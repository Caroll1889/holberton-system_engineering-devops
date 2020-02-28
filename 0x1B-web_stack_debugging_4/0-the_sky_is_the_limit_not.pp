# file

exec { 'fixed a request':
  command => '/bin/echo ULIMIT="-n 32768" | sudo tee /etc/default/nginx',
}

exec { 'nginx':
  command => '/usr/bin/service nginx restart'
}
