templates = {
  'home': 'index.html',
  'view': 'view.html'
}

routes = {
  'home': '/',
  'add': '/user/add',
  'view': '/user/<string:user_id>',
  'edit': '/user/<string:user_id>/edit',
  'remove': '/user/<string:user_id>/remove'
}