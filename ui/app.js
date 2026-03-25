const API_BASE = 'http://localhost:8000';
const sessionId = Math.random().toString(36).substring(2, 10);

document.getElementById('session-display').textContent = sessionId;

// Elements
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatMessages = document.getElementById('chat-messages');
const sendBtn = document.getElementById('send-btn');
const uploadForm = document.getElementById('upload-form');
const fileUpload = document.getElementById('file-upload');
const uploadStatus = document.getElementById('upload-status');

// Helper to escape HTML and format newlines
function formatText(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML.replace(/\n/g, '<br>');
}

function addMessage(content, sender, toolUsed = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender === 'user' ? 'user-message' : 'system-message'}`;
    
    let innerHTML = `
        <div class="avatar">${sender === 'user' ? 'U' : 'AI'}</div>
        <div class="message-content">
            ${formatText(content)}
            ${toolUsed ? `<div class="tool-badge">Tool: ${toolUsed}</div>` : ''}
        </div>
    `;
    
    messageDiv.innerHTML = innerHTML;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTyping() {
    const div = document.createElement('div');
    div.className = 'message system-message typing-indicator-container';
    div.id = 'typing-indicator';
    div.innerHTML = `
        <div class="avatar">AI</div>
        <div class="typing-indicator message-content">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    `;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTyping() {
    const ind = document.getElementById('typing-indicator');
    if (ind) ind.remove();
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = chatInput.value.trim();
    if (!query) return;
    
    // Add user message to UI
    addMessage(query, 'user');
    chatInput.value = '';
    sendBtn.disabled = true;
    showTyping();
    
    try {
        const res = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: query, session_id: sessionId })
        });
        
        const data = await res.json();
        removeTyping();
        
        if (res.ok) {
            addMessage(data.answer || data.detail || 'Success', 'system', data.tool_used);
        } else {
            addMessage(`Error: ${data.detail || 'Unknown server error'}`, 'system');
        }
        
    } catch (err) {
        removeTyping();
        addMessage(`Connection error: Make sure the server is running on ${API_BASE}`, 'system');
        console.error(err);
    } finally {
        sendBtn.disabled = false;
        chatInput.focus();
    }
});

uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const file = fileUpload.files[0];
    if (!file) {
        uploadStatus.textContent = 'Please select a file first.';
        uploadStatus.style.color = '#ef4444';
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    uploadStatus.textContent = 'Uploading and processing...';
    uploadStatus.style.color = '#94a3b8';
    document.getElementById('upload-btn').disabled = true;
    
    try {
        const res = await fetch(`${API_BASE}/upload-doc`, {
            method: 'POST',
            body: formData
        });
        
        if (res.ok) {
            uploadStatus.textContent = 'Upload successful!';
            uploadStatus.style.color = '#22c55e';
            fileUpload.value = '';
        } else {
            uploadStatus.textContent = 'Upload failed.';
            uploadStatus.style.color = '#ef4444';
        }
    } catch (err) {
        uploadStatus.textContent = 'Connection error.';
        uploadStatus.style.color = '#ef4444';
        console.error(err);
    } finally {
        document.getElementById('upload-btn').disabled = false;
    }
});

fileUpload.addEventListener('change', () => {
    if(fileUpload.files[0]) {
        uploadStatus.textContent = `Selected: ${fileUpload.files[0].name}`;
        uploadStatus.style.color = '#d8b4fe';
    }
});
