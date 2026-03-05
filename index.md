# MIMIR Dashboard

Welcome back. This is your central hub.

## Quick Access

- [[cockpit]] — Current week's focus
- [[system/vps]] — Server reference
- [[system/AGENTS]] — AI agent instructions

## Active Projects

${query[[from index.tag "page" where name =~ "^projects/" and name =~ "_context" order by lastModified desc]]}

## Recently Modified

${query[[from index.tag "page" order by lastModified desc limit 10]]}

## Folders

| Folder | Description |
|--------|-------------|
| [[projects/]] | Client projects and ISMS work |
| [[ai-trends/]] | Daily AI trend monitoring |
| [[calendar/]] | Weekly calendar extracts |
| [[system/]] | Config, VPS, agent instructions |

## Tasks This Week

${query[[from index.tag "task" where page =~ "^cockpit" and not done]]}

## How to Use This Space

1. **Create notes**: Press `Ctrl+k` (or `Cmd+k`) to open the page picker, type a name
2. **Link pages**: Use `[[Page Name]]` syntax for bi-directional links
3. **Add tasks**: Use `- [ ] Task description` for checkboxes
4. **Tag content**: Add `#tagname` anywhere in text
5. **Graph view**: Press `Ctrl+Shift+G` to see connections

---

_Last updated: ${Date.today()}_
