Research Group Web Site Template
================================

This is a [Jekyll][]-based Web site intended for research groups. Your group should be able to get up and running with minimal fuss.

<p align="center">
<img src="screenshot.png" width="387" height="225" alt="screenshot of the template">
</p>

This project originated at the University of Washington.  You can see the machinery working live at [our site][sampa].

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License][license].

[sampa]: http://sampa.cs.washington.edu/
[license]: https://creativecommons.org/licenses/by-nc/4.0/


Features
--------

* Thanks to [Jekyll][], content is just text files. So even faculty should be able to figure it out.
* Publications list generated from BibTeX.
* Personnel list. Organize your professors, students, staff, and alumni.
* Combined news stream and blog posts.
* Easily extensible navigation bar.
* Responsive (mobile-ready) design based on [Bootstrap][].

[Bootstrap]: http://getbootstrap.com/


Setup
-----

1. Install the dependencies. You will need [Python][], [bibble][] (`pip install bibble`), and [Jekyll][] (`gem install jekyll`).
2. [Fork][] this repository on GitHub.
3. Clone the fork to your own machine: `git clone git@github.com:yourgroup/research-group-web.git`.
4. Add an "upstream" remote for the original repository so you can stay abreast of bugfixes: `git remote add upstream https://github.com/uwsampa/research-group-web.git`.
5. Customize. Start with the `_config.yml` file, where you enter the name of the site and its URL.
6. Type `make` to build the site and then run `make serve` to view your site.
7. Keep adding content. See below for instructions for each of the various sections.
8. Periodically pull from the upstream repository: `git pull upstream master`.

[Python]: https://www.python.org/
[Fork]: https://github.com/uwsampa/research-group-web/fork


Publication List
----------------

The list of publications is in `bib/pubs.bib`. Typing `make` will generate `pubs.html`, which contains a pretty, sorted HTML-formatted list of papers. The public page, `publications.html`, also has a link to download the original BibTeX.


News Items and Blog Posts
-------------------------

For both long-form blog posts and short news updates, we use Jekyll's blogging system. To post a new item of either type, you create a file in the `_posts` directory using the naming convention `YYYY-MM-DD-title-for-url.md`. The date part of the filename always matters; the title part is currently only used for full blog posts (but is still required for news updates).

The file must begin with [YAML front matter][yfm]. For news updates, use this:

    ---
    layout: post
    shortnews: true
    ---

For full blog posts, use this format:

    ---
    layout: post
    title:  "Some Great Title Here"
    ---

And concoct a page title for your post. The body of the post goes after the `---` in either case.

You can also customize the icon that is displayed on the news feed. By default it's `newspaper-o`. We use icons from the [FontAwesome][fa] icon set.

The first paragraph of a post becomes its lead under the title (a leading "**Leiden, The Netherlands** –" is dropped there). Optional front matter for the post page:

- `type:` Shown next to the date, e.g. `Announcement`, `Papers`, `Podcast`.
- `image:` Shown in the side panel; `image_link:` makes it a link.
- `links:` Buttons in the side panel, e.g. `website:`, `video:`, `paper:`.
- `people:` Group members to show in the side panel, as keys from `_data/people.yml`, or `{key: stein, role: Chair}` to set the label.
- `projects:` Related projects, as `_projects` file names without `.md`.
- `papers:` A list of papers, rendered where the post body contains `{% include paper-list.html %}`. Each paper has `title`, and optionally `authors` (comma-separated; group members are shown in bold and listed in the side panel), `track` (e.g. `Hot Off the Press`; papers are grouped by track), `label`, `award`, `summary` (always shown), `abstract` (folded away) and `links` (`arxiv`, `doi`, `pdf`, `code`, `video`, `paper`).

[yfm]: http://jekyllrb.com/docs/frontmatter/
[fa]: http://fontawesome.io/icons/

Image thumbnails
----------------

Pages show small WebP copies of people photos, project images and news images from `img/thumbs/`. After adding or replacing an image in `img/people`, `img/projects` or `img/posts`, run `python make_thumbs.py` (needs Pillow) and commit the new files in `img/thumbs/`. If a thumbnail is missing, the page falls back to the original image, so nothing breaks, but the page gets heavier.


Projects
--------

To create a project, just create a markdown file in the `_projects` folder. Here are the things you can put in the YAML frontmatter:

- `title:` The project title.
- `notitle:` Set this to `true` if you don't want a title displayed on the project card. Optional.
- `description:` The text shown in the project card. It supports markdown.
- `people:` The people working on the project. This is a list of keys from the `_data/people.yml` file.
- `layout: project` This sets the layout of the actual project page. It should be set to `project`.
- `image:` The URL of an image for the project. This is shown on both the project page and the project card. Optional.
- `last-updated:` Date in the format of `YYYY-MM-DD`. The project cards are sorted by this, most recent first.
- `status: inactive` Set this to `inactive` if don't want the project to appear on the front page. Just ignore it otherwise.
- `featured: true` Show the project on the front page. At most six featured projects are shown (two rows), newest file name first; all projects are always listed on the Research page.
- `topics:` Research areas, as a list of keys from `research_areas` in `_config.yml` (`meta`, `xai`, `bench`, `genai`, `quantum`, `sustain`, `moo`). They label the card, drive the filter tabs on the Research page and pick related projects.
- `period:` Optional, e.g. `2024–2028`. Shown in the facts panel on the project page.
- `funder:` and `grant:` Optional. A funder containing "Horizon" or "European" shows the EU flag; one containing "NWO" shows the NWO logo.
- `partners:` Optional. A list of names (markdown links allowed) or one line of text.
- `links:` Optional map of buttons, e.g. `website:`, `github:`, `video:`, `news:`, `paper:`, `nwo:`.
- `projects:` Optional list of related projects. Without it, up to three current projects that share a topic are shown.
- `kind: line` Optional. Labels a long-running research line (like LLaMEA) as "Research line" instead of "Active".
- `awards:` Optional list of `{medal: gold|silver|bronze|winner, title, event, url}`, shown under the text.
- `publications:` Optional list of `{title, url, image, group}`, shown as a grid of cards below the text with filter tabs per `group`. Put the images in `img/llamea/` (or add another folder to `make_thumbs.py` and `_includes/thumb-src.html`).
- `link:` Set this to an external URL if this project has a page somewhere else on the web. If you don't have a `link:`, then the content of this markdown file (below the YAML frontmatter) will be this project's page.
- `no-link: true` Set this if you just don't want a project page for your project.

Personnel
---------

People are listed in a [YAML][] file in `_data/people.yml`. You can list the name, link, bio, and role of each person. Roles (e.g., "Faculty", "Staff", and "Students") are defined in `_config.yml`.

[YAML]: https://en.wikipedia.org/wiki/YAML


Building
--------

The requirements for building the site are:

* [Jekyll][]: run `gem install jekyll`
* [bibble][]: available on `pip`
* ssh and rsync, only if you want to deploy directly.

`make` compiles the bibliography and the website content to the `_site`
directory. To preview the site, run `jekyll serve`` and head to
http://0.0.0.0:5000.


Deploying to Your Sever
-----------------------

To set up deployments, edit the Makefile and look for the lines where `HOST` and `DIR` are defined. Change these to the host where your HTML files should be copied to.

To upload a new version of the site via rsync over ssh, type `make deploy`. A web hook does this automatically when you push to GitHub. Be aware that the Makefile is configured to have rsync delete stray files from the destination directory.

[Jekyll]: http://jekyllrb.com/
[bibble]: https://github.com/sampsyo/bibble/



### Run Python agents:

python -m client_server.game_agent_server --agent-module agents.random_agents --agent-class CarefulRandomAgent --port 9003
python -m client_server.game_agent_server --agent-module agents.greedy_heuristic_agent  --agent-class GreedyHeuristicAgent  --port 9004