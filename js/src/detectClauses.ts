import patterns from "./clauses.json";

export interface Detection {
  clause: string;
  pattern: string;
  snippet: string | null;
}

export function detectClauses(text: string): Detection[] {
  const results: Detection[] = [];

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

function extractSnippet(text: string, regex: RegExp): string | null {
  const match = text.match(regex);
  if (!match) return null;

  const start = Math.max(0, match.index! - 40);
  const end = Math.min(text.length, match.index! + 80);

  return text.substring(start, end) + "...";
}

