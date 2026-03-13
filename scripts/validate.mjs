#!/usr/bin/env node

/**
 * Validate all skills under skills/.
 *
 * Checks:
 * 1. Every skills/<slug>/ directory contains a SKILL.md
 * 2. SKILL.md has valid YAML frontmatter
 * 3. `name` is non-empty, lowercase hyphen-case, and matches directory name
 * 4. `description` is non-empty
 *
 * Zero dependencies — parses YAML frontmatter with simple regex extraction.
 */

import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const SKILLS_DIR = join(import.meta.dirname, "..", "skills");
const NAME_RE = /^[a-z0-9]+(-[a-z0-9]+)*$/;

function extractFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const raw = match[1];
  const fields = {};
  for (const line of raw.split(/\r?\n/)) {
    const kv = line.match(/^(\w[\w-]*):\s*(.+)/);
    if (kv) {
      let value = kv[2].trim();
      // Strip surrounding quotes
      if (
        (value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))
      ) {
        value = value.slice(1, -1);
      }
      fields[kv[1]] = value;
    }
  }
  return fields;
}

let errors = 0;
let skillCount = 0;

let entries;
try {
  entries = readdirSync(SKILLS_DIR);
} catch {
  console.log("No skills/ directory found. Nothing to validate.");
  process.exit(0);
}

const dirs = entries.filter((e) => {
  try {
    return statSync(join(SKILLS_DIR, e)).isDirectory();
  } catch {
    return false;
  }
});

if (dirs.length === 0) {
  console.log("No skill directories found. Nothing to validate.");
  process.exit(0);
}

for (const dir of dirs) {
  skillCount++;
  const skillPath = join(SKILLS_DIR, dir, "SKILL.md");

  let content;
  try {
    content = readFileSync(skillPath, "utf-8");
  } catch {
    console.error(`ERROR: ${dir}/ is missing SKILL.md`);
    errors++;
    continue;
  }

  const fm = extractFrontmatter(content);
  if (!fm) {
    console.error(`ERROR: ${dir}/SKILL.md has no valid YAML frontmatter`);
    errors++;
    continue;
  }

  if (!fm.name || fm.name.trim() === "") {
    console.error(`ERROR: ${dir}/SKILL.md frontmatter missing 'name'`);
    errors++;
  } else {
    if (!NAME_RE.test(fm.name)) {
      console.error(
        `ERROR: ${dir}/SKILL.md 'name' must be lowercase hyphen-case (got "${fm.name}")`
      );
      errors++;
    }
    if (fm.name !== dir) {
      console.error(
        `ERROR: ${dir}/SKILL.md 'name' ("${fm.name}") does not match directory name ("${dir}")`
      );
      errors++;
    }
  }

  if (!fm.description || fm.description.trim() === "") {
    console.error(`ERROR: ${dir}/SKILL.md frontmatter missing 'description'`);
    errors++;
  }
}

if (errors > 0) {
  console.error(`\nValidation failed with ${errors} error(s).`);
  process.exit(1);
} else {
  console.log(`Validated ${skillCount} skill(s). All passed.`);
}
