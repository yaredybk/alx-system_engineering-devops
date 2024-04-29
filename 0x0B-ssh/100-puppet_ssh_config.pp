# Puppet to make changes to our configuration file
# set up your client SSH configuration file to connect to a server
# without typing a password.

file { 'Turn off passwd auth':
  ensure  => present,
  content => 'PasswordAuthentication n\nIdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
}
