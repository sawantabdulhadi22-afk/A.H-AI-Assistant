const apiBase = "http://localhost:8000";

const chatBox = document.getElementById("chatBox");
const promptInput = document.getElementById("promptInput");
const sendBtn = document.getElementById("sendBtn");
const askBtn = document.getElementById("askBtn");
const voiceBtn = document.getElementById("voiceBtn");

function addMessage(text, sender = "bot") {
  const message = document.createElement("div");
  message.className = `message ${sender}`;
  message.textContent = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendPrompt() {
  const text = promptInput.value.trim();
  if (!text) return;

  addMessage(text, "user");
  promptInput.value = "";

  try {
    const response = await fetch(`${apiBase}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    const data = await response.json();
    addMessage(data.reply || "I could not process that request.", "bot");
  } catch (error) {
    addMessage("Backend not running. Start the FastAPI server first.", "bot");
  }
}

sendBtn.addEventListener("click", sendPrompt);
askBtn.addEventListener("click", () => {
  promptInput.focus();
});

voiceBtn.addEventListener("click", () => {
  addMessage("Voice mode is ready for future integration.", "bot");
});

promptInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendPrompt();
  }
});
