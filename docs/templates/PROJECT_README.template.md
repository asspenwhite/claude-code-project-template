# [Project Name]

[One-line description of what this project does]

---

## Quick Start

```bash
# Clone the repo
git clone [repo-url]
cd [project-name]

# Install dependencies
npm install

# Set up environment
cp .env.example .env.local
# Edit .env.local with your values

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Framework | Next.js 14 |
| Database | Supabase |
| Auth | Supabase Auth |
| Payments | Stripe |
| Styling | Tailwind CSS |
| UI Components | shadcn/ui |

---

## Project Structure

```
src/
├── app/              # Next.js pages and routes
│   ├── api/          # API routes
│   └── (routes)/     # Page routes
├── components/       # React components
│   ├── ui/           # shadcn/ui components
│   └── [feature]/    # Feature-specific components
├── lib/              # Utilities and configurations
│   ├── supabase/     # Database clients
│   └── utils.ts      # Helper functions
└── types/            # TypeScript types
```

---

## Environment Variables

Create `.env.local` with these variables:

```bash
# Supabase
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# Stripe
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

---

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run test` | Run tests |

---

## Documentation

| Document | Description |
|----------|-------------|
| [TODO.md](docs/TODO.md) | Active tasks and priorities |
| [CHANGELOG.md](docs/CHANGELOG.md) | Version history |
| [DECISIONS.md](docs/DECISIONS.md) | Architectural decisions |
| [API.md](docs/API.md) | API documentation |
| [SCHEMA.md](docs/SCHEMA.md) | Database schema |
| [LOGIC_AUDIT.md](docs/LOGIC_AUDIT.md) | User flow documentation |

---

## Development

### Prerequisites

- Node.js 18+
- npm or yarn
- Supabase account
- Stripe account (for payments)

### Local Development

1. Clone and install dependencies
2. Set up Supabase project
3. Configure environment variables
4. Run database migrations
5. Start development server

### Database Migrations

```bash
# Apply migrations
npx supabase db push

# Generate types
npx supabase gen types typescript --local > src/types/database.ts
```

---

## Deployment

### Production Checklist

- [ ] Environment variables set
- [ ] Database migrations applied
- [ ] Stripe webhook configured
- [ ] Domain configured
- [ ] SSL certificate active

### Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

---

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

---

## License

[MIT/Apache/etc.]

---

*Last updated: [Date]*
