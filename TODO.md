# TODO: Add User Accounts & Authentication and Collaborative Tasks

## 1. Configure Auth Settings
- [x] Update todoproject/settings.py to add LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL

## 2. Create Signup View and Template
- [x] Add signup view in tasks/views.py
- [x] Create tasks/templates/registration/signup.html template
- [x] Add signup URL to tasks/urls.py

## 3. Update Views for Authentication and User Assignment
- [x] Update index view to require login and filter tasks by user/shared
- [x] Update add_task view to assign user and require login
- [x] Update edit_task, delete_task, toggle_done views to require login and check ownership
- [x] Remove or update task_list view if not needed

## 4. Update Templates for Auth and Sharing
- [x] Update index.html to show login/logout/signup links, user-specific tasks, sharing UI
- [x] Update edit_task.html to include sharing form
- [x] Ensure login.html and logout.html are properly set up (create if empty)

## 5. Add Sharing Functionality
- [x] Add share_task view to allow sharing tasks with other users
- [x] Add URL for sharing
- [x] Update models if needed (already has shared_with field)
