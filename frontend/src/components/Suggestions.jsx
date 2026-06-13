import "./Suggestions.css";

function Suggestions({ questions, onSelect }) {

  if (!questions || questions.length === 0)
    return null;

  return (

    <div className="suggestions">

      <h4>
        Related Questions
      </h4>

      {

        questions.map((item, index) => (

          <button
            key={index}
            onClick={() => onSelect(item)}
          >

            {item}

          </button>

        ))

      }

    </div>

  );

}

export default Suggestions;