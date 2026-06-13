import "./Sidebar.css";

function Sidebar({ newChat, theme, setTheme }) {
  return (
    <div className="sidebar">

      <div className="logo">
        🤖 SmartFAQ AI
      </div>

      <button
        className="new-chat"
        onClick={newChat}
      >
        + New Chat
      </button>

      <button
        className="theme-btn"
        onClick={() =>
          setTheme(
            theme === "dark"
              ? "light"
              : "dark"
          )
        }
      >
        {theme === "dark"
          ? "☀️ Light Mode"
          : "🌙 Dark Mode"}
      </button>

    </div>
  );
}

export default Sidebar;