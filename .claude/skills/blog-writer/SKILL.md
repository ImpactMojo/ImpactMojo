---
name: blog-writer
description: Create new blog posts for impactmojo.in/blog with proper HTML template, napkin illustrations, blog.html card, and cross-references. Use when the user asks to write a blog post, add a blog entry, or create content for the blog.
---

# Blog Writer Skill

Create fully-formatted blog posts for ImpactMojo following the established template, illustration conventions, and cross-referencing requirements.

## When to Use

- User says "write a blog post about...", "new blog post", "add to the blog"
- User wants dev econ / education content published on impactmojo.in/blog

## Blog Post Template

Every post follows this structure:

### 1. File Creation

Create `blog/{slug}.html` using kebab-case naming.

### 2. HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Title} — ImpactMojo Blog</title>
    <meta property="og:title" content="{Title}">
    <meta property="og:description" content="{Excerpt}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.impactmojo.in/blog/{slug}.html">
    <meta property="article:author" content="The ImpactMojo Team">
    <meta property="article:published_time" content="{YYYY-MM-DD}">
    <meta property="article:section" content="{Category}">
    <meta property="article:tag" content="{Tag1}">
    <meta property="article:tag" content="{Tag2}">
    <!-- Copy CSS from an existing blog post (e.g., why-impactmojo-exists.html) -->
</head>
<body>
    <!-- Header nav (copy from existing post) -->
    <article>
        <header>
            <span class="category-badge {category}">{CATEGORY}</span>
            <h1>{Title}</h1>
            <div class="article-meta">
                <span class="article-date">{Month DD, YYYY}</span>
                <span class="article-readtime">{N} min</span>
            </div>
            <div class="article-tags">
                <span class="article-tag">{tag1}</span>
                <span class="article-tag">{tag2}</span>
            </div>
        </header>
        <div class="article-content">
            <!-- Blog content here -->

            <!-- Illustration 1 (after ~30% of content) -->
            <figure class="article-illustration">
                <img src="../assets/images/blog/{slug}/illustration-1.png"
                     alt="{Description}"
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <div style="display:none; padding: 3rem; background: var(--secondary-bg); border-radius: 12px;">
                    [Illustration 1: {Description}]
                </div>
                <figcaption>{Caption}</figcaption>
            </figure>

            <!-- More content -->

            <!-- Illustration 2 (after ~70% of content) -->
            <figure class="article-illustration">
                <img src="../assets/images/blog/{slug}/illustration-2.png"
                     alt="{Description}"
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <div style="display:none; padding: 3rem; background: var(--secondary-bg); border-radius: 12px;">
                    [Illustration 2: {Description}]
                </div>
                <figcaption>{Caption}</figcaption>
            </figure>
        </div>
        <!-- Share + Newsletter CTA + Related posts (copy from existing) -->
    </article>
    <!-- Footer (copy from existing) -->
</body>
</html>
```

### 3. Blog Categories & Colors

| Category | Code | Color |
|----------|------|-------|
| MEAL | `meal` | Green (#10B981) |
| Theory of Change | `toc` | Indigo (#6366F1) |
| Methods | `methods` | Sky Blue (#0EA5E9) |
| Stories | `stories` | Amber (#F59E0B) |
| Platform | `platform` | Pink (#EC4899) |

## Cross-Reference Checklist

After creating the blog post file:

1. **Add card to `blog.html`** — insert `<article class="blog-card">` with correct `data-category` and `data-tags`
2. **Create illustration directory** — `mkdir -p assets/images/blog/{slug}/`
3. **Generate napkin illustrations** — use napkin-ai skill to create 2 illustrations, save as `illustration-1.png` and `illustration-2.png`
4. **Add to search index** — add entry to `data/search-index.json`:
   ```json
   {"id": "BLOG{NNN}", "title": "...", "description": "...", "type": "blog", "category": "...", "url": "/blog/{slug}.html", "tags": [...]}
   ```
5. **Update sitemap.xml** — add `<url>` entry
6. **Update changelog** — add entry to `docs/changelog.md`

## Writing Guidelines

- **Evidence-backed**: cite specific studies, datasets, or frameworks
- **South Asian framing**: use examples from India, Bangladesh, Nepal, Sri Lanka
- **Practitioner voice**: write for NGO staff and researchers, not academics
- **Length**: 1,200–2,000 words (8–12 min read)
- **Structure**: Hook → Context → Core argument (with evidence) → Practical implications → Call to reflection
- **Author**: Always "The ImpactMojo Team"

## Best Practices

- Copy CSS and structural elements from the most recent blog post to ensure consistency
- Always include the onerror fallback for illustrations
- Set 2 related posts at the bottom linking to thematically relevant existing posts
- Date format in meta: `YYYY-MM-DD`, display format: `Month DD, YYYY`
