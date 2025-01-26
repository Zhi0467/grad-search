// ResultsList.js
// This React component displays a list of search results.
// It receives the results as a prop from its parent component and renders them as a list.
// Input: Array of search result objects (via props).
// Output: Rendered HTML list displaying the search results.
import React from "react";

const ResultsList = ({ results }) => (
    <ul>
        {results.map((result, index) => (
            <li key={index}>
                <h3>{result.name}</h3>
                <p>{result.description}</p>
            </li>
        ))}
    </ul>
);

export default ResultsList;
