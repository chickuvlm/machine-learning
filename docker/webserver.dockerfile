FROM container-default

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/start_webserver.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test

## executed everytime container starts
WORKDIR /var/machine-learning
CMD ["python", "app.py"]
