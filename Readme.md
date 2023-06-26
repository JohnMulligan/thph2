# Ostherr THPH site

## Specs

* Features
	* Google translate
	* Global search bar (not sure how to handle this other than an inexact match across all fields?)
* Pages
	* Flat
		* Homepage (w/ image carousel)
		* About, contact, etc.
		* Visualizations (all iframes from elsewhere)
	* Semi-flat
		* "Search all projects" page
		* Dropdown menus
		* All these come from 3 denormalized tables:
			* Humanities Field
			* Audience
			* Output type
		* 
		* Featured projects page (via a manual flag on individual items)
	* Individual project page template (dig into this)
		* Don't know how we'd do the related content footer
* Legacy migration
	* URL mapping 1:1 from the drupal site -- doable in urlpatterns?
	* CSS -- maintain/copy style as much as possible
* Site architecture
	* Django templated views w/ on-page js (e.g. for dropdown menus & search)
	* Elasticbeanstalk deployment (AWS) + S3 for assets
	* SQLite back-end
	* 100% repo-based (private) (GH)
	* Model-based Django admin interface [JCM]
	* Management commands for drawing in new surveys [JCM]
	* Domain name registration [JCM]
	

