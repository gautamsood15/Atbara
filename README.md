Video Management System

Project Features :-

1. Setup development env
2. Authentication django allauth
3. Register create channel
4. Edit Channel
5. upload Videos
6. Watch uploaded videos
7. like or dislike the video
8. comment on the video
9. Get the view count (anonymous | register)
10. edit video
11. delete video


# Model Structure

1. User

2. Category
    name (blog education, entertainment, technology)


3. Channel
    name
    user
    cannel art
    channel icon
    description
    category

4. Video
    id uuid
    video
    channel
    uploaded

5. VideoDetail
    videofile
    title
    description
    visibility
    thumbnail
    