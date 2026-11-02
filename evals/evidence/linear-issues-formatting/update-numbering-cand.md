I couldn't read the issue because Linear isn't connected. That means I haven't seen the existing comments, the issue key or the acceptance criteria. Below is a draft. Three things need your input before you post it.

```markdown
🤖 Written by Claude for [requester].

### Update

The email builder now has a Heading 4 option, and it is live on production.

**Added**
* **Heading 4:** users can now pick Heading 4 as a text style when they edit an email in the email builder.

[Screenshot of the Heading 4 option in the email builder]
```

**What you need to check:**

1. **Update number:** the team's convention is to number update comments. Use `### Update` if no existing comment starts with a `### Update` heading. If one does, use the next number, such as `### Update 2`. If you paste the existing comments here, I'll check them for you.
2. **Screenshot:** the convention asks for evidence of the result, so replace the placeholder with a screenshot or short video taken on production.
3. **Anything else that applies:** I only wrote what you told me. If any of these apply, tell me and I'll add sections:
   - **Changed:** existing headings were restyled.
   - **Known limitations:** the heading doesn't render the same in Outlook.
   - **Next steps:** existing templates need checking.

I didn't include PR links or a release date, because Linear already shows those.

**Outside the comment:**
- **Status:** this is a user-facing change, so **Done – Update Required** is probably the right status if the help centre article on text styles needs updating. I didn't change it.
- **Checkboxes:** tick the to-dos and acceptance criteria you verified on production. Leave the issue body as it is.
