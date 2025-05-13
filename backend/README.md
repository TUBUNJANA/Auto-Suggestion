# 🔍 AutoSuggestion Engine using Trie

This project implements a fast and efficient **autocomplete system** using the **Trie (prefix tree) data structure** in Python. It suggests the most relevant sentences based on user input, giving priority to historical frequency.

---

## 🚀 Features

- **Autocomplete Suggestions**: Get up to 10 suggestions based on the provided prefix.
- **Frequency-Based Prioritization**: Suggestions are ranked based on how often they appear.
- **Case-Insensitive Matching**: Handles user input in a case-insensitive manner.
- **Efficient Data Structure**: Utilizes the Trie data structure for rapid insertion and lookup.
- **Easy Debugging**: Provides an endpoint to retrieve the full trie structure for debugging purposes.

---

## ⚙️ Project Structure

- **main.py**: Contains the API endpoints using FastAPI.
- **trie.py**: Implements the Trie data structure and its operations.
- **requirements.txt**: Lists the dependencies for the project.

---

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd d:\PythonLLD\Auto Suggestion\backend
   ```

2. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Application

Run the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be accessible at [http://localhost:8000](http://localhost:8000).

---

## 📑 API Endpoints

- **GET /suggest?query=\<prefix\>**
  - Returns a list of sentence suggestions matching the provided prefix.
  - If no suggestions are found, the query is added to the Trie.
  
- **POST /add**
  - Adds a new sentence to the Trie.
  
- **GET /debug/trie**
  - Returns the complete Trie structure for debugging purposes.

---

## 📝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your proposed improvements and bug fixes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
