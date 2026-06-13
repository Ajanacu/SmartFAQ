import json
import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class FAQMatcher:
    def __init__(self):
        # Load a lightweight semantic model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load FAQ data
        data_path = os.path.join(
            os.path.dirname(__file__),
            "data",
            "faqs.json"
        )

        with open(data_path, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        # Store questions
        self.questions = [
            faq["question"]
            for faq in self.faqs
        ]

        # Compute embeddings once during startup
        self.embeddings = self.model.encode(
            self.questions,
            convert_to_tensor=False
        )

    def find_best_match(self, user_question):
        """
        Returns:
            matched FAQ
            confidence score
            related questions
        """
        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]   

        if user_question.lower().strip() in greetings:
            return {
                "matched_question": "Greeting",
                "answer": "👋 Hello! I'm SmartFAQ AI. How can I help you today?",
                "confidence": 100.0,
                "related_questions": [
                    "How do I reset my password?",
                    "How do I track my order?",
                    "How do I contact customer support?"
                ]
            }
        user_embedding = self.model.encode(
            [user_question],
            convert_to_tensor=False
        )

        similarities = cosine_similarity(
            user_embedding,
            self.embeddings
        )[0]

        best_index = similarities.argmax()

        best_faq = self.faqs[best_index]

        confidence = round(
            float(similarities[best_index]) * 100,
            2
        )
        if confidence < 55:
            return {
                "matched_question": "No Match",
                "answer": "Sorry, I couldn't find a relevant FAQ. Could you rephrase your question?",
                "confidence": confidence,
                "related_questions": []
            }

        # Find top related questions
        ranked_indices = similarities.argsort()[::-1]

        related_questions = []

        for idx in ranked_indices:
            if idx == best_index:
                continue

            related_questions.append(
                self.faqs[idx]["question"]
            )

            if len(related_questions) == 3:
                break

        return {
            "matched_question": best_faq["question"],
            "answer": best_faq["answer"],
            "confidence": confidence,
            "related_questions": related_questions
        }