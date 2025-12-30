# Before/After Examples

Real examples of AI slop vs distinctive design.

## Example 1: Hero Section

### AI Slop (Before)
```tsx
<section className="bg-white py-20">
  <div className="max-w-4xl mx-auto text-center">
    <h1 className="text-4xl font-bold text-gray-900">
      Welcome to Our Platform
    </h1>
    <p className="mt-4 text-gray-600">
      The best solution for your needs.
    </p>
    <button className="mt-8 bg-blue-500 text-white px-6 py-3 rounded-lg">
      Get Started
    </button>
  </div>
</section>
```

**Problems**: Generic fonts, centered layout, blue button, no visual interest

### Distinctive (After)
```tsx
<section className="relative min-h-[80vh] bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 overflow-hidden">
  {/* Background texture */}
  <div className="absolute inset-0 bg-[url('/grid.svg')] opacity-20" />

  <div className="relative max-w-6xl mx-auto px-6 py-24 flex items-center">
    <div className="max-w-2xl">
      <motion.span
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="inline-block px-3 py-1 text-xs font-medium tracking-wider uppercase text-amber-400 border border-amber-400/30 rounded-full mb-6"
      >
        New Feature Available
      </motion.span>

      <motion.h1
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="font-display text-5xl md:text-7xl font-bold text-white leading-[1.1] tracking-tight"
      >
        Build Something
        <span className="block text-amber-400">Amazing.</span>
      </motion.h1>

      <motion.p
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="mt-6 text-lg text-slate-300 max-w-lg"
      >
        The platform that helps you ship faster without compromising quality.
      </motion.p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="mt-8"
      >
        <button className="group relative px-8 py-4 bg-amber-500 text-slate-900 font-semibold rounded-lg overflow-hidden transition-transform hover:-translate-y-0.5">
          <span className="relative z-10">Get Started Free</span>
          <div className="absolute inset-0 bg-amber-400 translate-y-full group-hover:translate-y-0 transition-transform" />
        </button>
      </motion.div>
    </div>
  </div>
</section>
```

**Improvements**: Dark theme, gradient background, grid texture, staggered animations, distinctive typography, branded colors, asymmetric layout

---

## Example 2: Card Component

### AI Slop (Before)
```tsx
<div className="bg-white rounded-lg shadow p-6">
  <h3 className="text-lg font-semibold">Feature Title</h3>
  <p className="text-gray-500 mt-2">Feature description goes here.</p>
  <button className="mt-4 text-blue-500">Learn More →</button>
</div>
```

### Distinctive (After)
```tsx
<motion.div
  whileHover={{ y: -4 }}
  className="group relative bg-slate-800/50 backdrop-blur-sm rounded-xl p-6 border border-slate-700/50 overflow-hidden"
>
  {/* Gradient accent on hover */}
  <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-amber-500 to-orange-500 transform origin-left scale-x-0 group-hover:scale-x-100 transition-transform duration-300" />

  <div className="flex items-start gap-4">
    <div className="flex-shrink-0 w-12 h-12 rounded-lg bg-amber-500/10 flex items-center justify-center">
      <span className="text-2xl">✨</span>
    </div>

    <div className="flex-1">
      <div className="flex items-center gap-2">
        <h3 className="font-semibold text-white">Feature Title</h3>
        <span className="text-xs px-2 py-0.5 bg-emerald-500/20 text-emerald-400 rounded-full">
          New
        </span>
      </div>
      <p className="mt-2 text-sm text-slate-400">
        Feature description that provides real value.
      </p>
    </div>
  </div>

  <button className="mt-4 w-full py-2 text-sm font-medium text-amber-400 hover:text-amber-300 transition-colors flex items-center justify-center gap-2">
    Learn More
    <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
    </svg>
  </button>
</motion.div>
```

---

## Example 3: Form Input

### AI Slop (Before)
```tsx
<div>
  <label className="block text-sm text-gray-700">Email</label>
  <input
    type="email"
    className="mt-1 w-full border rounded px-3 py-2"
    placeholder="your@email.com"
  />
</div>
```

### Distinctive (After)
```tsx
<div className="relative">
  <input
    type="email"
    className="peer w-full bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-3 text-white placeholder-transparent focus:border-amber-500 focus:ring-2 focus:ring-amber-500/20 transition-all"
    placeholder="Email"
  />
  <label className="absolute left-4 -top-2.5 text-xs font-medium text-slate-400 bg-slate-900 px-1 peer-placeholder-shown:top-3 peer-placeholder-shown:text-base peer-placeholder-shown:text-slate-500 peer-focus:-top-2.5 peer-focus:text-xs peer-focus:text-amber-400 transition-all">
    Email Address
  </label>
</div>
```

---

## Example 4: Button

### AI Slop (Before)
```tsx
<button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
  Submit
</button>
```

### Distinctive (After)
```tsx
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
  className="relative group px-6 py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 font-semibold rounded-lg shadow-lg shadow-amber-500/25 overflow-hidden"
>
  <span className="relative z-10 flex items-center gap-2">
    Submit
    <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
    </svg>
  </span>
  <div className="absolute inset-0 bg-gradient-to-r from-orange-500 to-amber-500 opacity-0 group-hover:opacity-100 transition-opacity" />
</motion.button>
```

---

## Key Takeaways

1. **Add layers** - Backgrounds, textures, gradients create depth
2. **Animate purposefully** - Staggered entrances, hover states, micro-interactions
3. **Use brand colors** - Not generic blue/purple
4. **Break symmetry** - Asymmetric layouts are more interesting
5. **Add details** - Borders, shadows, badges, icons
