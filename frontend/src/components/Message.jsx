import "./Message.css";

function Message({ sender, text, confidence }) {
  return (
    <div className={`message ${sender}`}>

      <div className="bubble">

        <div className="text">
          {text}
        </div>

        {
          sender === "bot" &&
          confidence !== undefined && (
            <div className="confidence">

              🟢 Match

              <span>
                {confidence.toFixed(1)}%
              </span>

            </div>
          )
        }

      </div>

    </div>
  );
}

export default Message;