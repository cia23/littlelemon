The following API endpoints are implemented:

/admin/ : this gets you to the admin page
/restaurant/menu/ : see all items on the menu
/restaurant/menu/<int>/ : investigate a specific menu item. The integer is the ID of the menu item. This is the ID column of the table, IDs will not show in the restaurant/menu call
/restaurant/booking/ : see all the bookings
/auth/ : djoser API endpoints
/api-token-auth/ : get the token for the user