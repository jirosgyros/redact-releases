# Redact — Installers

Public download point for **Redact**, a desktop app for attorneys to redact PHI and other sensitive information from legal evidence. Files never leave your machine — all detection and redaction runs locally.

Source code is private. For source access or a tailored demo, contact the author.

## Download

Pick the file matching your operating system from the **[latest release](https://github.com/jirosgyros/redact-releases/releases/latest)**.

### Windows
- **`Redact_*_x64-setup.exe`** — NSIS installer, smaller file, recommended for individual installs
- **`Redact_*_x64_en-US.msi`** — MSI, for IT-managed deployments (Group Policy, Intune, etc.)

Requires Windows 10/11 64-bit. WebView2 Runtime is preinstalled on Windows 11; on Windows 10 the installer prompts to fetch it.

### macOS
- **`Redact_*_x64.dmg`** — Intel (x86_64). Runs on Apple Silicon via Rosetta 2.

Right-click the DMG → Open → drag Redact to Applications. On first launch, right-click the app → Open to bypass Gatekeeper.

## First-launch notes

The current builds **are not yet code-signed**. Operating systems will warn on first launch:

- **Windows SmartScreen**: "Windows protected your PC — Don't run." Click **More info** → **Run anyway**.
- **macOS Gatekeeper** (when shipped): "Redact can't be opened because Apple cannot check it for malicious software." Right-click the app in Applications → **Open**, then click **Open** in the dialog.

A signed build with no warnings is on the roadmap.

## What it does

1. Drag a PDF, DOCX, TXT, or image (PNG/JPG/TIFF/BMP/GIF/WEBP) onto the window.
2. The detector flags potential PHI — names, dates, SSNs, MRNs, phone numbers, addresses, insurance IDs, and more (HIPAA Safe Harbor + FRCP 5.2 presets).
3. Review each suggestion. Accept, reject, or draw your own redaction box.
4. Export. Output is a true content-stream redaction (not just a black box overlay) with metadata stripped and a post-export verify pass.

The first launch downloads a ~560 MB PHI detection model into your local cache (`%LOCALAPPDATA%\Redact\models\` on Windows). After that, startup is a few seconds.

## Privacy

- Working files live in the OS temp directory, overwritten before deletion at session close.
- No outbound network calls except the one-time model download on first launch.
- The audit log records hashes, counts, and timestamps — never document content or PHI text.

## Versions

| Version | Windows | macOS | Notes |
|---|---|---|---|
| `v0.1.4` | ✓ | ✓ | Highlight round-trip workflow, dark mode, phone number detection fix, yellow bleed fix |
| `v0.1.3` | ✓ | ✓ | First macOS build; OCR fallback for manual snap on image-derived PDFs |
| `v0.1.2` | ✓ | — | |
| `v0.1.1` | ✓ | — | |
| `v0.1.0` | ✓ | — | First Windows installer |
