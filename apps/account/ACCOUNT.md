# 🚀 Account App Documentation

## Purpose

The Account app manages **user identity across the ecosystem, ensuring:
✅ Consistent user model.
✅ Secure, scalable, clean architecture.
✅ Separation of identity (Account app) from authentication (tokens/OAuth).

---

## 📌 Architecture

* Account app: identity management only.
* Authentication handled externally via Simple JWT and third-party providers.
* User model: minimal, fast lookups, scalable for third-party auth.
* User profile: extended, flexible user data without bloating the User table.

---

## 🛠️ Models

### 1️⃣ `CustomUser`

A lean identity layer using `AbstractBaseUser` + `PermissionsMixin`:

* Fields:

  * `id`: UUID, primary key.
  * `email`: `USERNAME_FIELD`, unique, indexed.
  * `password`: `None` by default; `set_unusable_password()` if blank to support OAuth.
  * `is_active`, `is_staff`: Boolean flags.

* Manager (`CustomUserManager`):

  * `create_user`: Normalizes email, sets password if provided, else `set_unusable_password`.
  * `create_superuser`: Enforces `is_staff=True`, `is_superuser=True`.

Why `AbstractBaseUser`?
✅ Eliminates unused `username`, `first_name`, `last_name`.
✅ Forces intentional design of authentication flows.
✅ Supports email-only login cleanly.

---

### 2️⃣ `CustomUserProfile`

Linked via OneToOne to `CustomUser`, providing:

* `phone` (alt verification).
* `is_phone_verified`.
* `created_at`, `updated_at`.

✅ Keeps `CustomUser` minimal while extending flexibility for client apps.

---

## 🛡️ Admin Logic

* Custom `UserCreationForm`:

  * Adds password and confirmation.
  * Enforces match validation.

* Custom `UserChangeForm`:

  * Shows read-only password hash.

* `UserAdmin`:

  * Uses custom forms.
  * Displays email and permission flags.
  * Supports filtering, search, and ordering by email.
  * Uses `filter_horizontal` for groups and permissions.

✅ Enables a clean Django admin dashboard for user management without clutter.

---

## 🔄 Signals

* `create_profile`:

  * Automatically creates a `CustomUserProfile` when a `CustomUser` is created.

✅ Ensures every user has a profile without requiring manual intervention.

---

## Serializers
My serializers for account handles create, and delete therefore simplifying the view logic

## Views
### Create User




## OTP Verification (This prevent spamming of user creation)
flows

User creation
create_user







k






## 🌐 Third-Party Authentication Ready

* By default, `password=None` enables OAuth/third-party auth.
* Uses `set_unusable_password()` for accounts created via social login.
* Uses email consistency for cross-app identity.

✅ Supports scalable third-party auth without architecture changes.

---

## ✅ Summary

* Identity management only (auth handled by JWT/OAuth).
* Minimal `CustomUser` for fast auth and clean architecture.
* Flexible `CustomUserProfile` for extended data.
* Django admin integration for clean user management.
* Signals ensure profile lifecycle.

This design ensures your central authentication system remains scalable, clean, and easy to maintain.

---
