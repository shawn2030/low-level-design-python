[Requirements]

The task management system should allow users to create, update, and delete tasks.
Each task should have a title, description, due date, priority, and status (e.g., pending, in progress, completed).
Users should be able to assign tasks to other users and set reminders for tasks.
The system should support searching and filtering tasks based on various criteria (e.g., priority, due date, assigned user).
Users should be able to mark tasks as completed and view their task history.
The system should handle concurrent access to tasks and ensure data consistency.
The system should be extensible to accommodate future enhancements and new features.

[Actions]

task
-- title
-- descirption
-- task id -- random number generator
-- due date
-- priority
-- status {PENDING, IN PROGRESS, COMPLETED}
-- creator
-- assignee
-- reminder

status
-- PENDING
-- IN PROGERESS
-- COMPLETED

user
-- name
-- email id

system
-- user in system or not
    if yes
        print(hi User)
    else
        --create user
            -- enters user name i.e.
            -- enters email id

-- create task
    -- store task in task history
-- assign task
    -- store in task history
-- set reminder
    -- store in task history
-- set task complete
    -- store in task history
-- view task history
