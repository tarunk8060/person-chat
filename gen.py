def generate_response(persona, query, context):
    context_text = "\n".join(context[0])

    if persona == "Technical Expert":
        return f"""
Technical Analysis:
{context_text}

Issue detected: {query}
Suggested fix: Check API configuration and credentials.
"""

    elif persona == "Frustrated User":
        return f"""
I understand your frustration.

Possible solution:
{context_text}

We are working to resolve your issue quickly.
"""

    elif persona == "Business Executive":
        return f"""
Executive Summary:
{context_text}

Business impact:
Payment or service failures may affect revenue and customer trust.
"""

    else:
        return f"""
Support Response:
{context_text}
"""
