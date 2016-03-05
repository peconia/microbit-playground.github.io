# Jekyll plugin to load environment when running locally
# Plugins *not* loaded by github pages so uses default production values in _config.yml

module Jekyll
	class DevelopmentEnvironment < Generator
		def generate(site)
			site.config['url'] = 'http://localhost:4000'
			site.config['owner']['disqus-shortname'] = 'development_environment'
			site.config['google-tracking-code'] = '0000'
			site.config['sass']['style'] = 'expanded'
		end
  	end
end