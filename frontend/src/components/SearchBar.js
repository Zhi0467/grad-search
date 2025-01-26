// SearchBar.js
// This React component provides a search input field and a button to initiate a search.
// It sends the keyword to the backend `/search` endpoint and passes the results to a parent component.
// Input: Keyword (from user input).
// Output: Results fetched from the backend are passed to the parent component via a callback function.
import React, { useState } from "react";

const SearchBar = ({ onResults }) => {
    const [keyword, setKeyword] = useState("");

    const handleSearch = async () => {
        const response = await fetch("/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ keyword }),
        });
        const results = await response.json();
        onResults(results);
    };

    return (
        <div>
            <input
                type="text"
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
                placeholder="Search..."
            />
            <button onClick={handleSearch}>Search</button>
        </div>
    );
};

export default SearchBar;
