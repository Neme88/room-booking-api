## Git Workflow

This project follows a feature branch workflow to ensure clean and organized code management.

- **`main`**: The production-ready code. Only stable, tested code should be merged here.
- **`dev`**: The development branch where active development and integration occur.
- **`feature/*`**: Feature-specific branches branched off `dev`. Example:
  - `feature/room-booking-api`
  - `feature/user-authentication`
- **`hotfix/*`**: For critical fixes that need to be applied directly to `main`.

### Branching Example:
```bash
git checkout dev
git checkout -b feature/room-booking-api
# After development
git push origin feature/room-booking-api
