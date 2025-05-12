import React, { useState, useTransition } from "react";
import { TextField, List, ListItem, Paper } from "@mui/material";
import { getSuggestions } from "../api";

const SearchBar = () => {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    const value = e.target.value;
    setQuery(value);
    startTransition(async () => {
      if (value) {
        const data = await getSuggestions(value);
        setSuggestions(data.suggestions || []);
      } else {
        setSuggestions([]);
      }
    });
  };

  return (
    <div className="p-4 flex justify-center">
      <TextField
        label="Search"
        variant="outlined"
        value={query}
        onChange={handleChange}
        fullWidth
        // disabled={isPending}
      />
      {suggestions.length > 0 && (
        <Paper className="w-full mt-2">
          <List>
            {suggestions.map((item, index) => (
              <ListItem key={index}>{item}</ListItem>
            ))}
          </List>
        </Paper>
      )}
    </div>
  );
};

export default SearchBar;