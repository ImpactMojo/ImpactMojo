// InstantDB schema for ImpactLex
// Paste this into your InstantDB dashboard → Schema editor.
// Docs: https://www.instantdb.com/docs/modeling-data

import { i } from "@instantdb/core";

const _schema = i.schema({
  entities: {
    "$files": i.entity({
      "path": i.string().unique().indexed(),
      "url": i.string().optional(),
    }),
    "$users": i.entity({
      "email": i.string().unique().indexed().optional(),
      "imageURL": i.string().optional(),
      "type": i.string().optional(),
    }),
    "caseStudies": i.entity({
      "categories": i.any().optional(),
      "content": i.any().optional(),
      "country": i.any().optional(),
      "icon": i.any().optional(),
      "keyLessons": i.any().optional(),
      "region": i.any().optional(),
      "slug": i.any().optional(),
      "source": i.any().optional(),
      "sources": i.any().optional(),
      "summary": i.any().optional(),
      "title": i.any().optional(),
      "year": i.any().optional(),
    }),
    "formulae": i.entity({
      "category": i.any().optional(),
      "description": i.any().optional(),
      "formula": i.any().optional(),
      "fullExplanation": i.any().optional(),
      "name": i.any().optional(),
      "slug": i.any().optional(),
      "source": i.any().optional(),
    }),
    "terms": i.entity({
      "acronym": i.any().optional(),
      "aliases": i.any().optional(),
      "caseStudy": i.any().optional(),
      "category": i.any().optional(),
      "courses": i.any().optional(),
      "createdAt": i.any().optional(),
      "definition": i.any().optional(),
      "example": i.any().optional(),
      "formula": i.any().optional(),
      "related": i.any().optional(),
      "seedCategory": i.any().optional(),
      "slug": i.any().optional(),
      "source": i.any().optional(),
      "sources": i.any().optional(),
      "status": i.any().optional(),
      "term": i.any().optional(),
      "updatedAt": i.any().optional(),
    }),
    "contributions": i.entity({
      "term": i.string().optional(),
      "category": i.string().optional(),
      "definition": i.string().optional(),
      "example": i.string().optional(),
      "email": i.string().optional(),
      "status": i.string().optional(),
      "createdAt": i.string().optional(),
    }),
    "bookmarks": i.entity({
      "userId": i.string().indexed().optional(),
      "termId": i.string().indexed().optional(),
      "createdAt": i.string().optional(),
    }),
  },
  links: {
    "$usersLinkedPrimaryUser": {
      "forward": {
        "on": "$users",
        "has": "one",
        "label": "linkedPrimaryUser",
        "onDelete": "cascade"
      },
      "reverse": {
        "on": "$users",
        "has": "many",
        "label": "linkedGuestUsers"
      }
    }
  },
  rooms: {}
});

// This helps TypeScript display nicer intellisense
type _AppSchema = typeof _schema;
interface AppSchema extends _AppSchema {}
const schema: AppSchema = _schema;

export type { AppSchema }
export default schema;
