# 📄 Updated Requirement Specification – YouTube Front‑End MVP  

> **Purpose:** Capture all known constraints, design assets, performance goals, and deployment expectations for the MVP.  
> **Status:** *Partially completed* – three critical decisions remain **pending clarification** (see the highlighted “Open Items & Next Steps”).  

---

## 1. Scope & Vision  

| Item | Description |
|------|-------------|
| **MVP Focus** | Display a YouTube channel’s name, cover image, and video thumbnails. Minimal interaction (click‑through to a video detail view). |
| **Stretch Goals** | Theme toggle, user authentication, advanced analytics, SEO‑optimized server‑side rendering (if needed). |
| **Success Criteria** | • First Contentful Paint ≤ 1 s on typical 3G <br>• Bundle size ≤ 100 KB gzipped (code‑split entry point)<br>• Accessibility compliance – WCAG 2.1 AA<br>• Zero‑downtime deploy to the chosen hosting provider |

---

## 2. Technology Stack & Deployment  

| Decision | Options | **Chosen Value (Pending)** |
|----------|---------|----------------------------|
| **Bootstrap Tool** | CRA (Create‑React‑App) **or** Vite | **To be confirmed** |
| **Language** | JavaScript **or** TypeScript | **To be confirmed** |
| **Render Model** | SPA (client‑only) **or** SSR/SSG (Next.js, Remix) | **To be confirmed** |
| **Tailwind CSS** | Classic JIT vs. latest JIT (v3) | **To be confirmed** |
| **State Management** | useState / useReducer **or** Redux Toolkit / Zustand | **To be confirmed** |
| **Deployment Target** | Netlify **or** Vercel **or** Cloudflare Pages (static) / Vercel Edge Functions (SSR) | **To be confirmed** |
| **Package Manager** | npm **or** Yarn **or** pnpm | **Default → pnpm** |

> **Why it matters:** These choices drive the project scaffolding, CI/CD pipeline, build scripts, and runtime environment. **All decisions must be documented before development begins.**

---

## 3. Performance & Accessibility  

| Constraint | Target / Requirement | Rationale |
|------------|----------------------|-----------|
| **Bundle Size** | ≤ 100 KB gzipped (entry point) | Keeps load times low on limited bandwidth. |
| **First Contentful Paint (FCP)** | ≤ 1 s on 3G (≈ 2 s on 1 Mbps) | Directly impacts user experience & SEO. |
| **Bundle Splitting** | Lazy‑load route‑level components & image assets | Reduces initial payload. |
| **API Call Limits** | ≤ 2 concurrent fetches, respect YouTube quota (≤ 10 000 units/day) | Prevents hitting the YouTube quota. |
| **SEO / SSR** | *If SSR required*: pre‑render channel metadata; *If SPA*: provide `<meta>` tags via dynamic injection. | Improves discoverability. |
| **Accessibility** | WCAG 2.1 AA compliance (color contrast ≥ 4.5:1, keyboard navigation, ARIA labels) | Legal & UX best practice. |
| **Browser Support** | Chrome ≥ 90, Edge ≥ 90, Safari ≥ 14, Firefox ≥ 88. *Legacy* (IE11) **not** supported. |
| **Polyfills** | Only those required for the chosen runtime (e.g., `core-js` for older browsers). | Keeps bundle lean. |

---

## 4. Data & Feature Scope  

| Aspect | Details |
|--------|---------|
| **Data Source** | **Official YouTube Data API v3** (with API key). Authentication via a scoped API key; **rate‑limit awareness** required. |
| **Cache Strategy** | • In‑memory cache for channel data (TTL ≈ 5 min).<br>• Service‑worker / `Cache‑API` for static assets (images, icons).<br>• Stale‑while‑revalidate fallback for API responses. |
| **Pagination Model** | **Cursor‑based** pagination (`nextPageToken`) for video lists; **offset** not required. |
| **Extras (MVP)** | • **Theme toggle** (light / dark) – stored in `localStorage`.<br>• **Basic layout navigation** – channel view, video grid view.<br>• **Responsive image placeholders** (blur‑up). |
| **Non‑MVP (Stretch)** | • User authentication (Google OAuth).<br>• Personalised “watch‑later” playlists.<br>• Real‑time analytics dashboards. |
| **Testing Strategy** | • **Unit tests** – Jest/Vitest (≈ 80 % coverage).<br>• **End‑to‑End (E2E)** – Cypress or Playwright (core flows).<br>• **Accessibility audits** – axe‑core integration in CI. |

---

## 5. Timeline & Delivery Expectations  

| Milestone | Approx. Duration | Deliverable |
|-----------|------------------|-------------|
| **Kick‑off & Requirement Validation** | 1 week | Signed‑off spec, design assets, stack decisions. |
| **Scaffold & CI Setup** | 1 week | Repo, build pipelines (GitHub Actions), linting & formatting. |
| **Core Feature Implementation** | 2 weeks | Channel page, video grid, mock‑data fallback, basic theming. |
| **Data Integration & Caching** | 1 week | Real YouTube API integration, caching layer. |
| **Performance & Accessibility Optimization** | 1 week | Bundle analysis, FCP under 1 s, WCAG AA audit. |
| **Testing & QA** | 1 week | Unit/E2E test suite, CI quality gates. |
| **Pre‑Release Review & Bug‑Fixes** | 1 week | Deploy to staging, stakeholder feedback, final tweaks. |
| **Production Launch** | – | Deploy to production hosting. |

> **Buffer:** +1 week reserved for unforeseen blockers or design changes.

---

## 6. Design Assets & Style Guide  

| Requirement | Detail |
|-------------|--------|
| **Source Files** | Full Figma file (components, tokens, motion‑design specs) – preferred, else annotated style‑guide snippets. |
| **Brand Assets** | Hex colors, typography hierarchy, icon set, motion‑design keyframes. |
| **Component Library** | Re‑usable UI components (Button, Card, Loader, ThemeProvider). |
| **Export Conventions** | SVGs for icons, optimized PNG/WebP for thumbnails, `src/assets` folder structure. |

---

## 7. Deployment & Monitoring  

| Item | Requirement |
|------|-------------|
| **Hosting Provider** | To be confirmed (Netlify, Vercel, Cloudflare Pages, etc.). |
| **Build Scripts** | `npm run build` → outputs to `/dist` (or `.vercel/output`) compatible with CDN. |
| **Environment Variables** | `REACT_APP_YOUTUBE_API_KEY`, optional `NEXT_PUBLIC_…` prefixes if SSR is chosen. |
| **Analytics** | Google Analytics (gtag) – page view + custom event for channel interactions. |
| **Error Tracking** | Sentry (or similar) – send source‑map for production bugs. |
| **Health Checks** | `/healthz` endpoint (static) to verify CDN status; optional Vercel/Netlify function for uptime monitoring. |

---

## 8. Open Items & Next Steps  

| Category | Clarifying Question (Pending) | Owner | Due |
|----------|-------------------------------|-------|-----|
| **Technology Stack** | **What is the approved technology stack and deployment target?** (CRA vs. Vite, JS vs. TS, SPA vs. SSR/SSG, Netlify/Vercel/Cloudflare, Tailwind version, etc.) | Stakeholder | Within 3 business days |
| **Performance & Accessibility** | **Which non‑functional performance and accessibility targets are mandatory for the MVP?** (Bundle size, FCP, WCAG AA details, supported browsers, polyfill limits) | Stakeholder | Within 3 business days |
| **Data & Feature Scope** | **How will the UI consume YouTube data for the MVP launch?** (Official API vs. mock, caching strategy, required UI features such as theme toggle, auth, analytics) | Stakeholder | Within 3 business days |

### Immediate Action  
Schedule a short clarification call (≈ 30 min) with the stakeholder to answer the three bolded questions above. Once confirmed, replace the **Pending** entries with the definitive values, close the open‑item table, and mark the Requirement Specification as **Complete**.

---

## 9. The Three Most Critical Clarifying Questions  

1. **“What is the approved technology stack and deployment target?”**  
   *Do we proceed with CRA, Vite, or another starter? Will the app be a pure SPA, SSR/SSG, or static‑site? Which hosting provider (Netlify, Vercel, Cloudflare Pages, etc.) will be used?*  

2. **“Which non‑functional performance and accessibility targets are mandatory for the MVP?”**  
   *Specific bundle‑size ceiling, FCP target, WCAG 2.1 AA compliance criteria, supported browsers, and any polyfill restrictions?*  

3. **“How will the UI consume YouTube data for the MVP launch?”**  
   *Will we integrate the official YouTube Data API v3 from day 1 (with key and quota awareness) or rely on mock/fake data initially?*  
   *What caching strategy and extra UI features (theme toggle, authentication, analytics) are required for the MVP versus stretch goals?*  

---

### Final Note  

This updated specification captures every piece of information that **has been provided**. The three highlighted decisions remain **open** because the stakeholder elected to skip supplying those details.  

*When the stakeholder supplies answers to the questions above, the placeholders can be filled, the tables can be closed, and the document will be ready for hand‑off to design and development.*  

---  

*Prepared by the Requirement Management Team*  
*Date: 2025‑11‑02*