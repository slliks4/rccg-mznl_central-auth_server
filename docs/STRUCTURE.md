# Project Structure

This layout balances clarity, modularity, and scalability for a professional Django + DRF central authentication service, organized by feature-based apps with in-app docs.

```
central-auth/
├── .env.example
├── README.md           # High-level overview & links to features
├── requirements.txt    # Pin project dependencies
├── Dockerfile          # Container build instructions
├── docker-compose.yml  # Local dev + service orchestration
├── manage.py           # Django CLI entrypoint
├── config/             # Project configuration
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py     # Shared settings
│   │   ├── dev.py      # Development overrides
│   │   └── prod.py     # Production overrides
│   ├── urls.py         # Root URL routes
│   └── wsgi.py         # WSGI entrypoint
├── apps/               # Feature-based Django apps
│   ├── auth/           # Authentication core & integration
│   │   ├── docs/       # auth feature documentation (AUTH.md)
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── auth.py     # Core token obtain/refresh/logout logic
│   │   ├── features/   # Additional auth features
│   │   │   └── oauth/   # OAuth integrations (Google, GitHub, etc.)
│   │   ├── permissions.py  # DRF permission classes
│   │   ├── services/   # auth-related helpers (jwt, token blacklisting)
│   │   ├── urls.py     # auth endpoints
│   │   └── views/      # DRF views for auth flows
│   ├── account/        # User profile & account management
│   │   ├── docs/       # account feature documentation (ACCOUNT.md)
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py   # CustomUser + CustomUserManager
│   │   ├── serializers.py
│   │   ├── signals.py  # e.g. on_create, on_delete hooks
│   │   ├── services/   # account-related business logic
│   │   ├── urls.py
│   │   └── views/      # DRF views for /register, /me, etc.
│   └── profiles/      # Example consuming app handling user profiles
│       ├── docs/      # feature documentation
│       └── ...
├── core/              # Cross-cutting utilities
│   ├── __init__.py
│   ├── exceptions.py
│   ├── mixins.py
│   └── utils.py
├── docs/              # Project-level documentation
│   ├── Structure.md   # This file
│   ├── DEPLOYMENT.md  # Deployment guides
ation
    ├── start.sh│   └── DESIGN.md      # Architecture and design decisions
└── scripts/           # Developer tooling & autom
    ├── migrate.sh
    └── seed_data.sh
```

---

## Design Rationale

* Feature-based apps (`apps/auth`, `apps/account`) let teams work on isolated concerns simultaneously, enhancing parallel development and reducing merge conflicts.
* In-app `docs/` folders (e.g. `apps/auth/docs/AUTH.md`) keep feature documentation adjacent to code, improving discoverability for maintainers.
* `auth/auth.py`as core: Holds token obtain, refresh, and logout logic; additional flows (e.g. OAuth) live under `features/` subfolders.
* `account/`app: Focuses on user model, registration, profile lifecycle, and signal hooks—separating identity data from authentication flows.
* `core/` utilities: Shared exceptions, mixins, and helpers to avoid duplication across apps.
* Project `docs/`: Houses overarching docs (deployment, architecture) applicable to the entire codebase.
* Modular services layer: Each app’s `services/` contains pure-Python logic (e.g. OTP generation, token blacklisting) for easy unit testing.
* Scalability & Professionalism: This layout supports horizontal scaling, microservice extraction, and clear boundaries—critical for enterprise-grade systems.
