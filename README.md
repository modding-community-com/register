# Modding Community Subdomain Registry

This repository allows community members to register their own `*.modding-community.com` subdomains via GitHub Pull Requests. By submitting a configuration file to this repository, you can point a custom subdomain to your project hosted on GitHub Pages, Vercel, Netlify, or a self-hosted server.

---

## Rules and Limitations

To maintain the integrity of the registry, the following rules are enforced:

* **One Subdomain Per Target:** Each target URL (e.g., your GitHub Pages URL or server IP) can only be associated with a single subdomain in this registry. This prevents duplicate entries for the same project.
* **Unique Filenames:** Your JSON filename must exactly match your requested subdomain. For example, if you want `cool-mod.modding-community.com`, your file must be named `cool-mod.json`.
* **Manual Approval:** All requests are manually reviewed. Subdomains that are offensive, misleading, or impersonate other projects will be rejected.
* **Active Content:** Subdomains pointing to broken or empty sites may be removed periodically to free up names for active community projects.
* **Reporting a site:** If you would like to report a subdomain, please DM me (@atomictyler on discord).

---

## How to Register

1. **Fork this repository** to your own GitHub account.
2. **Create a new JSON file** in the `domains/` directory. The filename must be `your-subdomain.json`.
3. **Define your configuration** using the JSON structure (subdomain, type, and target).
4. **Submit a Pull Request** from your fork to our `main` branch.
5. **Validation:** Automated scripts will check for duplicates and formatting errors. If the checks pass and the content is appropriate, a maintainer will merge the PR. Your domain will be live within minutes of the merge.

```json
{
    "subdomain": "your-subdomain",
    "type": "CNAME",
    "target": "your-username.github.io"
}
```

> [!NOTE]
> This is not limited to GitHub pages!

---

## Hosting Setup Instructions

Once your Pull Request has been merged, you must configure your hosting provider to accept incoming traffic from your new subdomain.

### GitHub Pages
1. Navigate to your project repository on GitHub.
2. Go to **Settings** > **Pages**.
3. Under the **Custom Domain** section, enter `your-subdomain.modding-community.com`.
4. Click **Save**. GitHub will verify the DNS record and generate an SSL certificate for you.

### Vercel, Netlify, or Other Cloud Platforms
1. Open your project dashboard on your hosting provider (e.g., Vercel or Netlify).
2. Locate the **Domain Settings** or **Custom Domains** section.
3. Add `your-subdomain.modding-community.com` as a new domain.
4. The provider will automatically detect the CNAME record managed by our Cloudflare configuration.

### Self-Hosted (A Records)
If you are hosting your project on a VPS, dedicated server, or home lab:
1. In your JSON file, set the type to "A".
2. Set the target to your server's public IPv4 address.
3. Configure your web server (such as Nginx, Apache, or Caddy) to listen for the specific hostname `your-subdomain.modding-community.com`.

---

## Modifying or Deleting a Subdomain

* **To update:** Edit your existing JSON file in the `domains/` folder (e.g., to change the target URL) and submit a new Pull Request.
* **To delete:** Submit a Pull Request that deletes your JSON file from the `domains/` folder.

Once the PR is merged, our automated synchronization script will update or remove the DNS record from Cloudflare accordingly.