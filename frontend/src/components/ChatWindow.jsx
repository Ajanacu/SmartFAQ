import { useState, useRef, useEffect } from "react";
import axios from "axios";

import "./ChatWindow.css";

import Message from "./Message";
import Suggestions from "./Suggestions";
import TypingIndicator from "./TypingIndicator";

const API = process.env.REACT_APP_API;

function ChatWindow({ reset }) {

  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [typing, setTyping] = useState(false);
  const [related, setRelated] = useState([]);

  const bottomRef = useRef();

  // auto scroll
  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [messages, typing]);

  // reset chat (New Chat)
  useEffect(() => {
    setMessages([]);
    setInput("");
    setRelated([]);
    setTyping(false);
  }, [reset]);

  async function sendQuestion(question = input) {

    if (!question.trim()) return;

    const userMessage = {
      sender: "user",
      text: question
    };

    setMessages(prev => [...prev, userMessage]);
    setInput("");
    setTyping(true);

    try {

      const res = await axios.post(`${API}/chat`, {
        question
      });

      const botMessage = {
        sender: "bot",
        text: res.data.answer,
        confidence: res.data.confidence
      };

      setTyping(false);

      setMessages(prev => [...prev, botMessage]);
      setRelated(res.data.related_questions || []);

    } catch (err) {

      setTyping(false);

      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to server."
        }
      ]);

    }
  }

  return (
    <div className="chat-window">

      {/* CHAT AREA */}
      <div className="chat-area">

        {messages.length === 0 ? (

          <div className="welcome-screen">

            <h1>🤖 SmartFAQ AI</h1>

            <p>How can I help today?</p>

            <div className="popular">

              <button onClick={() => sendQuestion("How do I reset my password?")}>
                Reset Password
              </button>

              <button onClick={() => sendQuestion("How do I track my order?")}>
                Track Order
              </button>

              <button onClick={() => sendQuestion("What is your refund policy?")}>
                Refund Policy
              </button>

              <button onClick={() => sendQuestion("How do I contact customer support?")}>
                Contact Support
              </button>

            </div>

          </div>

        ) : (

          <div className="messages">

            {messages.map((msg, index) => (
              <Message
                key={index}
                sender={msg.sender}
                text={msg.text}
                confidence={msg.confidence}
              />
            ))}

            {typing && <TypingIndicator />}

            <div ref={bottomRef} />

          </div>

        )}

      </div>

      {/* SUGGESTIONS */}
      <Suggestions
        questions={related}
        onSelect={sendQuestion}
      />

      {/* INPUT */}
      <div className="input-area">

        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") sendQuestion();
          }}
          placeholder="Ask anything..."
        />

        <button onClick={() => sendQuestion()}>
          Send
        </button>

      </div>

    </div>
  );
}

export default ChatWindow;