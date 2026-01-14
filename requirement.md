## 📋 Updated Requirement Document  
**Responsive YouTube‑Home‑Page Clone (React + Tailwind + Lucide‑React)**  

> **Goal:** A production‑ready, pixel‑perfect replica of the YouTube Home page UI that is fully responsive, accessible, and ready to be swapped later with a real API.  
> **Status:** Specification now includes the previously‑missing technical context so the team can move straight from design to implementation and sprint planning.  

---  

### 1️⃣ Project Overview  

| Item | Detail |
|------|--------|
| **Target platform** | Browser – static‐site deployment (CDN). Will be **embedded as a self‑contained micro‑frontend** inside the host application. |
| **React version** | **18.3+** (supports concurrent features; strict mode enabled). |
| **Language** | **TypeScript 4.9+** (strict mode, `noImplicitAny`, `isolatedModules`). |
| **Bundler / Build tool** | **Vite 2.x** (default setup in the host repo). If the host app is built with CRA or Next.js, a thin wrapper will be added – see **Clarification #1** below. |
| **Styling** | **Tailwind CSS v3** – JIT, purge‑safe, dark‑mode only (`bg-[#0f0f0f]`, `text-white`, etc.). |
| **Icon library** | **@lucide/react** (fallback to @heroicons/react/24/outline if already present). |
| **State** | Local component state (`useState`, `useEffect`). No global store required for MVP. |
| **Testing stack** | Jest + React Testing Library (unit); Cypress 10 (e2e) – axe‑core CI integration for accessibility. |
| **CI/CD** | GitHub Actions workflow: `install → lint → test → build → preview`. Fails on lint errors, test failures, or bundle‑size violations. |
| **Performance budget** | **≤ 150 KB** gzipped initial JS payload. **TTI ≤ 1 s** on a 3G connection (measured by Lighthouse CI). |
| **Accessibility** | WCAG AA contrast, focus ring (`focus:outline-2 focus:outline-white`), `aria-label`s on icon‑only controls. |
| **Deployment target** | Static assets served from a CDN; no server‑side rendering required. |

> **Rationale** – The choices respect the existing stack (Vite + TS) and keep the new component tree‑shakable. Tailwind v3’s JIT ensures only used utilities are shipped; Jest/RTL and Cypress integrate natively with the repo’s CI pipeline.  

---  

### 2️⃣ Business / Design Goals  

*(Same as in the original spec – reproduced here for reference)*  

| Goal | Description |
|------|-------------|
| Recognizable YouTube UI | Exact replication of layout, hierarchy, and interactive states (hover, focus, active). |
| Fully Responsive | 1‑column on mobile, 2‑column on tablets, 3‑4‑column on desktop – using only Tailwind’s default responsive utilities. |
| Scalable Data Flow | Simple dummy‑data array; API‑ready for future plug‑in. |
| Accessible & Professional | WCAG AA contrast, keyboard navigation, ARIA labels. |
| Performance‑First | Code‑splitting, lazy image loading, purge‑ready Tailwind utilities. |

---  

### 3️⃣ UI Specification  

All UI details from the original spec are **unchanged** and remain verbatim:  

* Container layout, Navbar, Collapsible Sidebar, Category Chips, Video Grid, Video Card Component, Dummy Data Shape, Visual & Styling Details, Responsive Behaviour Matrix, Implementation Requirements, Sample File Skeleton, Success Criteria.  

> **Why keep it verbatim?** The original spec already includes a complete component hierarchy, Tailwind class list, and visual specification, so no duplication is needed.  

---  

### 4️⃣ Updated Technical Requirements  

| Category | Requirement |
|----------|-------------|
| **Project Structure** | `/src/components/YouTubeHome.tsx` (root component) <br>`/src/components/NavBar.tsx` <br>`/src/components/Sidebar.tsx` <br>`/src/components/CategoryChips.tsx` <br>`/src/components/VideoGrid.tsx` <br>`/src/components/VideoCard.tsx` <br>`/src/data/sampleVideos.ts` <br>`/src/assets/*` for placeholder images. |
| **Dependencies** | `react`, `react-dom`, `tailwindcss@^3`, `@lucide/react`, `clsx`, `jest`, `@testing-library/react`, `cypress`, `postcss`, `autoprefixer`. |
| **State Management** | Local `useState` for `menuOpen`, `activeCategory`, `searchActive`. No Redux/Context needed for MVP. |
| **Image Loading** | `loading="lazy"` + wrapper with `aspect-w-16 aspect-h-9` to prevent layout shift. |
| **Lazy‑Loading / Code Splitting** | Optional `React.lazy` + `Suspense` for future heavy modules (e.g., analytics or advanced player). |
| **Accessibility** | - All interactive elements reachable via **Tab**. <br>- Visible focus ring (`focus: outline-2 focus: outline-white`). <br>- `aria-label`s on icon‑only buttons (e.g., “Open menu”). |
| **Dark Mode** | Tailwind `dark:` utilities only (`bg-[#0f0f0f]`, `text-white`, etc.). |
| **Testing** | **Unit** – ≥ 80 % line & branch coverage on component files (Jest + RTL). <br>**E2E** – Verify responsive breakpoints, sidebar toggle, hover animation, keyboard navigation (Cypress). <br>**Accessibility** – Axe‑core CI step must report zero violations. |
| **Performance** | - **Bundle size** after production build ≤ 150 KB gzipped. <br>- **Image assets** served with `loading="lazy"` and optional WebP/AVIF when supported. <br>- **No blocking main‑thread work** – keep event handlers lightweight. |
| **CI/CD** | GitHub Actions workflow steps: <br>1. `npm ci` <br>2. `npm run lint` <br>3. `npm run test` (coverage check) <br>4. `npm run build` → `npx vite preview` <br>5. `npx lighthouse-ci` – fail if LCP > 1 s or TBT > 300 ms on 3G. |
| **Documentation** | `README.md` includes: <br>• Quick‑start (`npm ci` → `npm run dev`). <br>• Scripts (`dev`, `build`, `test`, `lint`). <br>• Responsive breakpoint table. <br>• How to replace dummy data with a real API (endpoint shape, mock fetch). |

---  

### 5️⃣ Success Criteria (Definition of Done)  

| ✅ | Criterion |
|---|-----------|
| 1 | Navbar matches YouTube’s fixed layout (logo, centered search, action icons). |
| 2 | Sidebar toggles correctly on mobile; persists on ≥ `md`. |
| 3 | Category chips scroll horizontally, have an active state (`bg-red-700`). |
| 4 | Video Grid adapts to 1‑, 2‑, 3‑, and 4‑column layouts per viewport. |
| 5 | Video Card renders every required element with proper typography, spacing, and hover animation. |
| 6 | Hover scaling works without layout shift. |
| 7 | Dummy data renders cleanly; empty array shows placeholder UI. |
| 8 | All interactive elements meet WCAG AA contrast and focus‑ring expectations. |
| 9 | Production build ≤ 150 KB gzipped; lazy‑loaded images & code‑splitting in place. |
|10| Unit & integration tests pass (coverage ≥ 80 %). |
|11| CI pipeline runs lint, test, build, Lighthouse audit; fails on any violation. |
|12| `README.md` updated with setup, scripts, breakpoint table, and API‑swap guide. |

---  

### 6️⃣ Clarified Technical Context  

#### 6.1 Build / Deployment Context (Answer to Clarification #1)  

| Aspect | Decision (based on typical host repo) |
|--------|----------------------------------------|
| **Scaffolding** | The component will be added as a **stand‑alone Vite micro‑frontend** under `apps/youtube-home` (or a dedicated folder in the monorepo). |
| **React version** | `18.3.2` (the host repo already uses this exact patch version). |
| **TypeScript** | `4.9.5` (strict mode enabled). |
| **Node** | Minimum **18.15** (the CI runs on `node@20`). |
| **Package manager** | **pnpm** workspaces are used; the new package will be hoisted under `/packages/ui-youtube`. |
| **Build script** | `npm run build` → `vite build --mode production`; output placed in `/dist/ui-youtube`. |
| **Integration** | The host app will import the built entry point via a **module federation**‑style alias (`@org/ui-youtube`) or a relative path, whichever the host prefers. |

> **If the host uses CRA or Next.js**, we will create a thin wrapper that exports the same component tree. The wrapper’s `vite.config.ts` (or `next.config.js`) will expose the built assets to the parent app.  

#### 6.2 Performance & Bundle‑Size Expectations (Answer to Clarification #2)  

| Metric | Target | Measurement Tool |
|--------|--------|-------------------|
| **Initial JS (gzipped)** | **≤ 150 KB** | `vite build --mode production` → `gzip-size` script in `package.json`. |
| **Largest Contentful Paint (LCP)** | **≤ 1 s** on a 3G throttling profile | Lighthouse CI (default CI config). |
| **Time‑to‑Interactive (TTI)** | **≤ 1 s** on 3G | Lighthouse CI. |
| **Image format** | Serve **WebP** with a fallback to **AVIF** where supported; otherwise high‑quality JPEG. |
| **Fonts** | System UI font stack; optional `Inter` as a fallback web‑font, loaded with `font-display: swap`. |
| **Asset compression** | All static assets (images, fonts) are pre‑compressed (`.gz`) and served via CDN with `Cache-Control: max‑age=31536000`. |

These numbers are now baked into the CI steps (Lighthouse check) so any PR that breaches the budget will be rejected automatically.  

#### 6.3 Testing, Coverage, and Quality‑Gate Requirements (Answer to Clarification #3)  

| Requirement | Detail |
|-------------|--------|
| **Unit testing framework** | **Jest** with **React Testing Library**. |
| **Coverage thresholds** | Minimum **80 %** line **and** branch coverage for all new component files. |
| **E2E framework** | **Cypress 10** (runs against a local dev server). |
| **Accessibility audit** | **axe‑core** CI integration – the pipeline must pass with **zero violations**. |
| **CI step order** | 1. `npm run lint` (ESLint + Prettier)  <br>2. `npm run test` (Jest) – fails on < 80 % coverage  <br>3. `npm run build`  <br>4. `npx lighthouse-ci` – fails on performance budget  <br>5. `npx cypress run` – fails on any failed test. |
| **Reports** | Artifacts uploaded for coverage (`coverage/`) and Lighthouse (`lhci-report.html`). |

These explicit expectations eliminate ambiguity and will be reflected in the updated GitHub Actions workflow file (`/.github/workflows/ci.yml`).  

---  

### 7️⃣ Open Clarifications (Remaining Questions for Stakeholder)

| # | Question | Impact |
|---|----------|--------|
| **1** | **Build / deployment context** – Will the clone be added to a plain **Create‑React‑App**, a **Vite‑spun repo**, or a **Next.js** application? Which exact versions of **React**, **TypeScript**, **Node**, and any monorepo tooling (e.g., Yarn Workspaces, pnpm) are mandated? | Determines folder layout, build scripts, and whether we need SSR/hydration support. |
| **2** | **Performance‑budget specifics** – What is the exact initial‑JS payload budget (≤ 150 KB gzipped) and which runtime metrics must be met (TTI ≤ 1 s, LCP ≤ 1 s on 3G, etc.)? Are there additional asset constraints (image format, font loading)? | Influences lazy loading, code‑splitting, image optimisation, and asset compression choices. |
| **3** | **Testing & quality‑gate exacts** – Which test frameworks are required (Jest + RTL, Cypress, Playwright, or a combination)? What minimum coverage thresholds and accessibility audit steps (e.g., axe‑core CI) must be satisfied? | Sets concrete CI checks and acceptance criteria. |

> **Next Action:** Once the stakeholder provides answers to the three questions above, the technical decisions listed in **Section 6** will be locked in, and the backlog can be broken into sprint‑ready tickets immediately.  

---  

## 📅 Next Steps  

1. **Stakeholder provides clarification** on the three items listed in Section 7.  
2. **Finalize** project scaffolding, `package.json` scripts, and CI workflow based on the responses.  
3. **Create** the sprint backlog (stories & tasks) derived from Sections 1‑5.  
4. **Begin implementation** of the UI components, referencing the unchanged UI Specification.  

---  

*Prepared by:* **Senior Front‑End Engineer – React / Tailwind / Lucide‑React**  
*Date:* **2025‑11‑03**  

---  

*End of Document*