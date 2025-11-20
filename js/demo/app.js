async function loadPatterns() {
  const res = await fetch("../src/clauses.json");
  return await res.json();
}

function detectClauses(text, patterns) {
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

document.getElementById("scanBtn").onclick = async () => {
  const file = document.getElementById("fileInput").files[0];
  if (!file) return alert("Upload a contract first!");

  const text = await file.text();
  const patterns = await loadPatterns();

  const results = detectClauses(text, patterns);

  document.getElementById("results").textContent =
    JSON.stringify(results, null, 2);
};

