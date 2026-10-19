# Status: setup prepared, live execution NOT started

The worker requires this repository to be PRIVATE before loading image metadata or contacting Shopify. No image manifest or credentials have been uploaded. Do not add credentials to source files.

431 images remain. Code changes only image alt and filename, preserves extension, visually checks each image twice, saves a checkpoint before a live write, compares current values and reads back both values. Uncertain outcomes stop for review.

Required GitHub Actions Secrets after privacy is verified: SHOPIFY_SHOP, SHOPIFY_ACCESS_TOKEN, GEMINI_API_KEY. Shopify credential requires product reads and file reads/writes; do not grant theme, customer or order permissions. The existing ChatGPT plugin credential cannot be exported to a cloud runner.

Use a Gemini free-tier project without billing and standard GitHub-hosted runners within remaining included minutes; paid Actions spending must stay zero. Quota exhaustion stops processing; overnight completion is not guaranteed. First live test must be one image with independent read-back. No schedule is enabled.

Repository privacy and GitHub plugin write access must be resolved before the image manifest or Actions workflow is added. The public-repository manifest upload was refused by approval review; do not bypass it.
