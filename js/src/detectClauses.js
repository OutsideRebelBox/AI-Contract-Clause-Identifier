const fs = require("fs");

function loadPatterns() {
  return JSON.parse(fs.readFileSync(__dirname + "/clauses.json", "utf8"));
}

function detectClauses(text) {
  const patterns = loadPatterns();
  const results = [];

  for (const [clauseName, regexList] of Object.entries(patterns)) {
    regexList.forEach((pattern) => {
      const regex = new RegExp(pattern, "i");

      if (regex.test(text)) {
        results.push({
          clause: clauseName,
          pattern,
          snippet: extractSnippet(text, regex),
        });
      }
    });
  }

  return results;
}

function extractSnippet(text, regex) {
  const match = text.match(regex);
  if (!match) return null;

  const start = Math.max(0, match.index - 40);
  const end = Math.min(text.length, match.index + 80);

  return text.substring(start, end) + "...";
}

module.exports = { detectClauses };

