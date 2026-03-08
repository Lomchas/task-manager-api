## System Design

### Entities:
- User
- Task

### Relationship:
User 1 -> N Tasks

### Endpoints:
POST /auth/register
POST /auth/login
GET /tasks
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}