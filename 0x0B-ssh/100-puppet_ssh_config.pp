# Puppet to make changes to our configuration file
# set up your client SSH configuration file to connect to a server
# without typing a password.

file { 'Turn off passwd auth':
  ensure  => present,
  content <<-'EOF'
Host *
        passwordAuthentification no
        IdentifyFile ~/.ssh/school
EOF
  path    => '/etc/ssh/ssh_config',
}
