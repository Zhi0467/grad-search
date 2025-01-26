// App.js
// This file is the main entry point for the frontend application.
// It integrates the SearchBar and ResultsList components, managing their state and interactions.
// Input: None directly; manages state for keyword and results.
// Output: Renders the full UI with a search bar and results list.

import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";

const App = () => {
    const [results, setResults] = useState([]);

    return (
        <div>
            <h1>Grad School Search</h1>
            <SearchBar onResults={setResults} />
            <ResultsList results={results} />
        </div>
    );
};

export default App;
