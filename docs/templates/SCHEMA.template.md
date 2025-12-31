# [Project Name] - Database Schema

Database structure, relationships, and access policies.

---

## Table of Contents

- [Connection Info](#connection-info)
- [Tables Overview](#tables-overview)
- [Table Details](#table-details)
- [RLS Policies](#rls-policies)
- [Indexes](#indexes)
- [Common Queries](#common-queries)
- [Migrations](#migrations)

---

## Connection Info

- **Provider:** [Supabase/PlanetScale/etc.]
- **Project ID:** `[project-id]`
- **Dashboard:** [URL]

---

## Tables Overview

| Table | Purpose | RLS Policy |
|-------|---------|------------|
| `users` | User accounts | User owns own |
| `[table]` | [Purpose] | [Policy type] |

---

## Table Details

### users

Extended user profile data.

| Column | Type | Nullable | Default | Notes |
|--------|------|----------|---------|-------|
| `id` | uuid | No | - | PK, FK to auth.users |
| `email` | text | No | - | Unique |
| `full_name` | text | Yes | - | |
| `created_at` | timestamptz | No | now() | |
| `updated_at` | timestamptz | No | now() | |

**Relationships:**
- `id` → `auth.users.id` (one-to-one)

---

### [table_name]

[Description of table purpose]

| Column | Type | Nullable | Default | Notes |
|--------|------|----------|---------|-------|
| `id` | uuid | No | gen_random_uuid() | PK |
| `user_id` | uuid | No | - | FK to users |
| `[column]` | [type] | [Yes/No] | [default] | [notes] |
| `created_at` | timestamptz | No | now() | |

**Relationships:**
- `user_id` → `users.id` (many-to-one)

**Constraints:**
- Unique: `(user_id, [column])`

---

## RLS Policies

### [table_name]

```sql
-- Users can read their own records
CREATE POLICY "Users can read own [table]"
ON [table_name] FOR SELECT
USING (auth.uid() = user_id);

-- Users can create their own records
CREATE POLICY "Users can create own [table]"
ON [table_name] FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- Users can update their own records
CREATE POLICY "Users can update own [table]"
ON [table_name] FOR UPDATE
USING (auth.uid() = user_id);

-- Users can delete their own records
CREATE POLICY "Users can delete own [table]"
ON [table_name] FOR DELETE
USING (auth.uid() = user_id);
```

### Public read tables

```sql
-- Anyone can read (reference data)
CREATE POLICY "Public read access"
ON [table_name] FOR SELECT
USING (true);
```

### Admin-only tables

```sql
-- No RLS - use service role only
ALTER TABLE [table_name] ENABLE ROW LEVEL SECURITY;
-- No policies = service role only
```

---

## Indexes

```sql
-- Fast lookup by user
CREATE INDEX idx_[table]_user_id
ON [table_name](user_id);

-- Fast lookup by [field]
CREATE INDEX idx_[table]_[field]
ON [table_name]([field]);

-- Unique constraint with condition
CREATE UNIQUE INDEX idx_[table]_unique_[condition]
ON [table_name] (user_id) WHERE [condition];
```

---

## Common Queries

### Get User's [Resources]

```sql
SELECT * FROM [table_name]
WHERE user_id = $1
ORDER BY created_at DESC;
```

### Check if [Condition]

```sql
SELECT EXISTS (
  SELECT 1 FROM [table_name]
  WHERE user_id = $1
  AND [condition]
) as exists;
```

### Create [Resource]

```sql
INSERT INTO [table_name] (user_id, [columns])
VALUES ($1, $2)
RETURNING *;
```

### Update [Resource]

```sql
UPDATE [table_name]
SET [column] = $2, updated_at = now()
WHERE id = $1 AND user_id = auth.uid()
RETURNING *;
```

---

## Migrations

### Create table

```sql
-- Migration: create_[table]_table
-- Created: [Date]

CREATE TABLE [table_name] (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  [column] [type] [constraints],
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

-- Enable RLS
ALTER TABLE [table_name] ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can read own [table]"
ON [table_name] FOR SELECT USING (auth.uid() = user_id);

-- Create indexes
CREATE INDEX idx_[table]_user_id ON [table_name](user_id);
```

### Add column

```sql
-- Migration: add_[column]_to_[table]
-- Created: [Date]

ALTER TABLE [table_name]
ADD COLUMN [column_name] [type] [constraints];
```

---

## Triggers

### Updated at trigger

```sql
-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER [table]_updated_at
BEFORE UPDATE ON [table_name]
FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

---

*Last updated: [Date]*
