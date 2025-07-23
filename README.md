# Central Authentication Service

A centralized authentication system built with Django REST Framework (DRF) to manage user identity, verification, and session management across multiple applications.

---
## 🚀 What You’ll Get (MVP Scope)

1. Custom User Model
   * UUID primary key, email as `USERNAME_FIELD`, optional phone and avatar.
   * Why: Provides a flexible identity schema and consistent user ID across apps.

3. JWT Authentication
   * Endpoints for token obtain/refresh via DRF Simple JWT.
   * Why: Offers stateless, scalable sessions suited to SPAs and microservices.
   * Setup Blacklist and Rotate refresh tokens for security
   * setup CORS
 
4. User Info Endpoint (`/api/account/me/`)
   * Returns ID, email, pic, roles, and groups(contain permissions).
   * Why: Standardizes identity checks for all consumer apps without re‑implementing logic.

5. Environment‑Driven Configuration
   * `.env` support via `django-environ`.
   * Why: Aligns with 12‑factor principles and secures sensitive credentials.

## ✅ MVP Scope (Now)

- [x] `/auth/register/`  
  - Validate email (unique)
  - Validate password (Django password validators)
  - Save user with `set_password()`

- [x] `/auth/token/`  
  - Use `TokenObtainPairView`

- [x] `/auth/token/refresh/`  
  - Use `TokenRefreshView`

- [x] `/account/me`  
  - Use `TokenRefreshView`

## 📚 Documentation

* [AUTH.md](./apps/auth/AUTH.md) — In‑depth overview of authentication flows, endpoints, and token management.
* [ACCOUNT.md](./apps/account/ACCOUNT.md) — Detailed CustomUser model, account lifecycle, and profile management.
* [STRUCTURE.md](./docs/STRUCTURE.md) — Project Structure
* [DEPLOYMENT.md](./docs/DEPLOYMENT.md) — Deployment steps and Docs

---


---

## 🔜 Post‑MVP & Future Updates
This document outlines upcoming features and enhancements for the authentication system that will be added after MVP launch. The current version includes only:

### 🔐 OTP Email Verification

- [ ] `/auth/register/start/`  
  - Validates email/password
  - Throttled by IP/email
  - Sends hashed 6-digit OTP via email
  - Signature create
  - Stores temporary data in Redis (or cache backend)

- [ ] `/auth/register/confirm/`  
  - verifies signature before it proceeds
  - Validates OTP
  - On success, creates user

- [ ] Cache store: Redis or Memcached  
  - Set up for OTP + future throttling

### 🚫 Throttling & Anti-Spam

- [ ] Per-IP and per-email throttling on OTP endpoints  
- [ ] Add reCAPTCHA (if needed) for public routes  
- [ ] Debounce email to prevent OTP flood

### 📬 Email System

- [ ] Integrate SMTP or third-party (e.g., SendGrid)  
- [ ] Add backend for templated email sending  
- [ ] Support async email queue (via Celery)

### 🔄 Password Reset

- [ ] `/auth/password/reset/`  
  - Accepts email, sends reset link (signed token)

- [ ] `/auth/password/reset/confirm/`  
  - Accepts token + new password
  - Validates strength

### 📱 Forgot Email (Phone Verified)

- [ ] `/auth/email/lookup/`  
  - Accepts phone number
  - Returns masked email(s) if phone matches verified user

### 🛡️ Production Settings (JWT & Cache)

- [ ] Configure Simple JWT securely:
  - Access token: 15m
  - Refresh token: 7d
  - Rotation + blacklist support

- [ ] Setup production cache backend:
  - Replace LocMemCache with Redis
  - Configure timeouts, security

### 🧩 Nice to have Add-ons

- [ ] Social login (Google, Apple) via `django-allauth`  
- [ ] Email magic links  
- [ ] Admin audit logging for auth attempts  
- [ ] 2FA (SMS or TOTP)  
- [ ] Session revocation and login history  

* Lifecycle Hooks (`on_create`, `on_update`, `on_delete`)
  Notify downstream apps of account events for data federation.

* Public/Private Key Trust Model
  Sign requests from central auth and verify in sub‑apps for tamper‑proof communication.

* Registered Applications Registry
  Dynamic service discovery for profile provisioning and deletion.

* Asynchronous Sync Queues (Celery/RQ)
  Reliable background jobs with retry/backoff and monitoring dashboards.

---

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
