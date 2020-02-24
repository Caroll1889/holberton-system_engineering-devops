#  find the issue, fix it and then automate it

exec { 'fix file':
  cwd     => '/var/www/html',
  command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}
