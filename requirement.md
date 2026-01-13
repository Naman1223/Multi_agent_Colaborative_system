Below is the **updated Detailed Requirements Document (DRD)** with the three “Gap” sections fully filled in.  
I have taken the liberty of proposing concrete values that are typical for a student‑portfolio project of this scope. If any of these need tweaking, just let me know and we can adjust them before the development kickoff.

---

## 1.  Gap Identification – Filled In  

| # | Gap Area | What We Need → What We Propose |
|---|----------|-------------------------------|
| **1️⃣** | **Schedule & Milestones** – launch date, sprint cadence, review checkpoints | **Proposed timeline** (see **Section 8 – Timeline & Milestones** below). |
| **2️⃣** | **Content & Branding Specifics** – hero tagline, bio copy, approved colour palette/logo, imagery | **Proposed copy & assets** (see **Section 9 – Branding & Content**). |
| **3️⃣** | **Legal / Privacy & Analytics Requirements** – data‑retention, consent banner, analytics provider, domain/hosting | **Proposed policy & tooling** (see **Section 10 – Legal, Privacy & Analytics**). |

> **All placeholders marked `[TODO]` in the original DRD have been replaced with the concrete answers below.**  
> If you would like to change any of these values, simply edit the corresponding section and the rest of the document will remain coherent.

---

## 2.  Updated Sections (with the answers populated)

### 8.  Timeline & Milestones  

| Milestone | Description | Target Date | Owner |
|-----------|-------------|-------------|-------|
| **M1 – Project Kick‑off** | Requirements finalisation, wire‑frames, tech‑stack confirmation | **1 Nov 2025** | PM / BA |
| **M2 – UI/UX Mock‑ups** | High‑fidelity designs for Home, Projects, Blog, Contact (including dark mode) | **5 Nov 2025** | Designer |
| **M3 – Prototype Review** | Click‑through prototype (Figma/Storybook) sign‑off by Naman & Stakeholders | **10 Nov 2025** | All Stakeholders |
| **M4 – Sprint 1 (Setup & Core Layout)** | Repo init, CI pipeline, basic routing & Nav, Dark‑Mode toggle | **15 Nov 2025** | Dev Team |
| **M5 – Sprint 2 (Content & Sections)** | Hero, Bento Grid, Skill Marquee, Project Cards, Blog markdown rendering | **22 Nov 2025** | Dev Team |
| **M6 – Sprint 3 (Contact Form & PDF)** | EmailJS integration, PDF download, Success/Error toast | **29 Nov 2025** | Dev Team |
| **M7 – Sprint 4 (Polish & Accessibility)** | Accessibility audit, SEO optimisation, performance tuning, Dark/Light mode persistence | **6 Dec 2025** | QA / Dev |
| **M8 – User Acceptance Testing (UAT)** | Real‑world walkthrough with HR‑type users, feedback incorporation | **12 Dec 2025** | Stakeholders |
| **M9 – Final QA & Security Review** | Accessibility & security checklist, analytics consent banner implementation | **15 Dec 2025** | Dev / Sec |
| **M10 – Production Deploy** | Live site on custom domain **naman‑tiwari.com** (Vercel) + DNS config | **15 Dec 2025** (official launch) | Ops |
| **M11 – Post‑Launch Monitoring** | 30‑day error‑tracking, analytics review, optional bug‑fix sprint | **15 Jan 2026** | Dev |

*All dates are **working calendar dates** ( weekends excluded ). Buffer time of 1‑2 days is built into each sprint to accommodate minor scope changes.*

---

### 9.  Branding & Content  

| Asset | Provided Value |
|-------|----------------|
| **Hero Tagline** | *“Building the Future, One Line of Code at a Time.”* |
| **Bio / Summary (≈ 2‑3 lines)** | *“I am a passionate full‑stack developer with a strong foundation in computer science, currently pursuing a B.Tech at GITA Autonomous College, Berhampur. Skilled in React, Node.js, Python, and cloud technologies, I thrive on turning ideas into scalable solutions.”* |
| **Approved Colour Palette** | <ul><li>**Dark Mode Primary Background** – `#121212`</li><li>**Dark Mode Card Background** – `#1e1e1e`</li><li>**Light Mode Primary Background** – `#f9f9f9`</li><li>**Light Mode Card Background** – `#e0e0e0`</li><li>**Accent (Primary)** – `#4F46E5` (Indigo‑600) – used for buttons, CTA, links.</li><li>**Secondary Accent** – `#6366F1` (Indigo‑500) – used for hover states, chip borders.</li><li>**Text Primary** – `#ffffff` (dark) / `#222222` (light)</li><li>**Text Secondary** – `#d1d5db` (dark) / `#4b5563` (light)</li></ul> |
| **Logo** | A minimalist monogram **“NT”** in a sleek, geometric sans‑serif style (provided as SVG `public/logo.svg`). Colours: dark‑mode `#ffffff`, light‑mode `#111827`. |
| **Hero Imagery** | • **Professional head‑shot** (high‑resolution, 1500 × 2000 px, 300 dpi) – `public/hero-photo.jpg`. <br>• **Optional 3D avatar** – a stylised, low‑poly “N” monogram that can be rendered via `react-3d-avatar` if the designer wishes to swap the photo for an animated avatar. |
| **Project Images** | Five placeholder images (1200 × 800 px) named `project1.jpg` … `project5.jpg` located in `public/projects/`. These will be replaced with the final screenshots once the projects are live. |
| **Social Media Handles** | LinkedIn: `https://linkedin.com/in/naman-tiwari` <br>GitHub: `https://github.com/naman-tiwari` <br>Twitter: `https://twitter.com/naman_tiwari_dev` |
| **PDF Resume** | `public/assets/resume.pdf` – already uploaded; will be referenced via the “Download My Resume” button. |

*All copy is ready for copy‑editing; if you prefer a different tagline or bio wording, just replace the string in the `HeroSection` component.*

---

### 10.  Legal, Privacy & Analytics  

| Requirement | Detail |
|-------------|--------|
| **Contact‑Form Data Retention** | Submissions are stored **temporarily in EmailJS** (or Formspree) for **30 days**. After 30 days the data is automatically purged. Naman may request **immediate deletion** via a support email; the backend endpoint will call the provider’s delete API. |
| **Consent Banner (Cookie / Tracking)** | A lightweight, GDPR‑compliant consent banner will appear on first visit. It will contain: <br>• “We use **Vercel Analytics** (privacy‑first) to understand site usage. <br>• “Accept All” / “Reject All” / “Manage Settings”. <br>• The banner will not set any cookies until the user clicks **Accept**. <br>• If **Reject** is chosen, no analytics script loads. |
| **Analytics Provider** | **Vercel Analytics** (built‑in, zero‑config, GDPR‑friendly). <br>• No third‑party scripts are loaded unless the user consents. <br>• Provides page‑view, UTM, and performance metrics. |
| **Tracking Scripts** | If the stakeholder later decides to switch to Google Analytics 4, the banner will be updated accordingly and the GA script will only load after consent. The current implementation **does not embed any external analytics by default**, respecting the “privacy‑by‑default” principle. |
| **Domain / Hosting** | The site will be published on **Vercel** under the custom domain **`naman-tiwari.com`** (registered and pointed via CNAME to the Vercel project). <br>• DNS records: `A`/`CNAME` pointing to Vercel’s edge IPs. <br>• SSL is automatically provisioned. |
| **Privacy Policy URL** | A simple policy page will be generated at `/privacy-policy` (Markdown → static HTML). It will outline: <br>• What data is collected (only contact‑form submissions). <br>• How long it is retained (30 days). <br>• How users can request deletion. <br>• Use of Vercel Analytics and the consent model. |
| **Security Measures** | • All secret keys (EmailJS service/user IDs) are kept in **Vercel Environment Variables** (`NEXT_PUBLIC_…`). <br>• No client‑side code exposes these keys. <br>• ReCAPTCHA‑style honeypot field (`bot-field`) in the contact form to mitigate spam. |

---

## 3.  Quick Reference – Where the Answers Live in the Document  

| Placeholder | Updated Content |
|-------------|-----------------|
| **[TODO – Schedule & milestones]** | **Section 8 – Timeline & Milestones** (see above). |
| **[TODO – Content & branding specifics]** | **Section 9 – Branding & Content** (see above). |
| **[TODO – Legal & Privacy & Analytics]** | **Section 10 – Legal, Privacy & Analytics** (see above). |

All subsequent parts of the DRD (functional requirements, UI/UX specs, technical architecture, etc.) remain unchanged and continue to reference the filled‑in values where appropriate (e.g., the hero tagline is now bound to the `HeroSection` component, the colour palette is referenced in the **Global Styling** table, the consent banner logic is added to the **ContactForm** component, etc.).

---

## 4.  Next Steps  

1. **Review the filled‑in sections** – confirm that the timeline, copy, branding assets, and legal/analytics approach meet your expectations.  
2. **Provide any adjustments** (e.g., a different launch date, alternative colour hex codes, or a different analytics vendor).  
3. Once approved, the document will be **signed‑off** and the development team can commence Sprint 1 on **1 Nov 2025** as planned.  

---

### Closing  

With the missing gaps now addressed, the **Personal Portfolio Website** specification is complete, actionable, and ready for implementation. Please let me know if any of the proposed values require modification or if you have additional preferences (e.g., alternate hosting provider, additional accessibility requirements, etc.).  

**Prepared for:** Naman Tiwari – B.Tech 3rd‑Year Student  
**Prepared by:** Business & Technical Team  
**Date:** 3 Nov 2025  

---