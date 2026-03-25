from sqlalchemy.orm import Session
from app.services.rag import retrieve_relevant_chunks
from app.services.llm import generate_response
from app.services.memory import get_history, save_message
from app.services.tools import summarize_text, extract_action_items


def chat_with_agent(query: str, db: Session, session_id: str):
    history = get_history(session_id)

    tool = decide_tool(query)

    if tool == "summarize":
        chunks = retrieve_relevant_chunks(query, db)
        text = "\n".join(chunks)
        answer = summarize_text(text)

    elif tool == "actions":
        chunks = retrieve_relevant_chunks(query, db)
        text = "\n".join(chunks)
        answer = extract_action_items(text)

    else:  # RAG
        chunks = retrieve_relevant_chunks(query, db)
        answer = generate_response(query, chunks, history)

    # save memory
    save_message(session_id, "user", query)
    save_message(session_id, "assistant", answer)

    return {
        "answer": answer,
        "tool_used": tool
    }


def decide_tool(query: str):
    query_lower = query.lower()

    if "summarize" in query_lower:
        return "summarize"
    elif "action items" in query_lower or "tasks" in query_lower:
        return "actions"
    else:
        return "rag"