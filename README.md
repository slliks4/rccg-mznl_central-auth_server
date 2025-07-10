# Central Authentication Service

A centralized authentication system built with Django REST Framework (DRF) to manage user identity, verification, and session management across multiple applications.

---
## 🚀 What You’ll Get (MVP Scope)

1. Custom User Model
   * UUID primary key, email as `USERNAME_FIELD`, optional phone and avatar.
   * Why: Provides a flexible identity schema and consistent user ID across apps.

2. OTP Email Verification
   * Cache‑backed, hashed one‑time codes (5–10 min TTL).
   * Why: Prevents spam sign‑ups and ensures valid email ownership before DB writes.

3. JWT Authentication
   * Endpoints for token obtain/refresh via DRF Simple JWT.
   * Why: Offers stateless, scalable sessions suited to SPAs and microservices.

4. User Info Endpoint (`/api/account/me/`)
   * Returns ID, email, pic, roles, and groups(contain permissions).
   * Why: Standardizes identity checks for all consumer apps without re‑implementing logic.

5. Environment‑Driven Configuration
   * `.env` support via `django-environ`.
   * Why: Aligns with 12‑factor principles and secures sensitive credentials.

6. Rate Limiting & Throttling
   * Protects `/send-otp/` and `/verify-otp/` from abuse.
   * Why: Ensures system availability and defends against brute‑force attacks.

---

## 📚 Documentation

* [AUTH.md](./apps/auth/AUTH.md) — In‑depth overview of authentication flows, endpoints, and token management.
* [ACCOUNT.md](./apps/account/ACCOUNT.md) — Detailed CustomUser model, account lifecycle, and profile management.
* [STRUCTURE.md](./docs/STRUCTURE.md) — Project Structure
* [DEPLOYMENT.md](./docs/DEPLOYMENT.md) — Deployment steps and Docs

---

## 🔜 Post‑MVP & Future Updates

After your first client is integrated, we’ll expand with:

* Lifecycle Hooks (`on_create`, `on_update`, `on_delete`)
  Notify downstream apps of account events for data federation.

* Public/Private Key Trust Model
  Sign requests from central auth and verify in sub‑apps for tamper‑proof communication.

* Registered Applications Registry
  Dynamic service discovery for profile provisioning and deletion.

* Asynchronous Sync Queues (Celery/RQ)
  Reliable background jobs with retry/backoff and monitoring dashboards.

---

## 🎯 Professional Rationale

1. Lean MVP First
   Focus on core identity, verification, and session flows to deliver value quickly.
2. Security‑By‑Design
   Hashed OTPs, HTTPS‑only cookies, short‑lived JWTs, and rate limits guard against common threats.
3. Scalable Patterns
   Stateless JWT and cache‑driven OTPs permit horizontal scaling without session affinity.
4. 12‑Factor Compliance
   Environment‑based settings and modular design ease deployment to any cloud or container platform.

---

> For full endpoint references, data models, and implementation details, please refer to ./apps/auth/AUTH.md and ./apps/account/ACCOUNT.md.
