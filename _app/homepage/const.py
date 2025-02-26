from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class WebAuthnExample:
    language: str
    url: str
    title: str
    author: str
    type: Union[Literal["Library"], Literal["Demo"]]


# Various WebAuthn-related libraries
libraries = [
    WebAuthnExample(
        language="Python",
        url="https://github.com/duo-labs/py_webauthn",
        title="duo-labs/py_webauthn",
        author="Duo Labs",
        type="Library",
    ),
    WebAuthnExample(
        language="TypeScript",
        url="https://github.com/MasterKale/SimpleWebAuthn",
        title="SimpleWebAuthn",
        author="Matthew Miller",
        type="Library",
    ),
    WebAuthnExample(
        language="TypeScript",
        url="https://github.com/passwordless-id/webauthn",
        title="passwordless-id/webauthn",
        author="Arnaud Dagnelies",
        type="Library",
    ),
    WebAuthnExample(
        language="Ruby",
        url="https://github.com/cedarcode/webauthn-ruby",
        title="cedarcode/webauthn-ruby",
        author="Cedarcode",
        type="Library",
    ),
    WebAuthnExample(
        language="Ruby",
        url="https://github.com/ruby-passkeys/devise-passkeys",
        title="ruby-passkeys/devise-passkeys",
        author="Ruby passkeys",
        type="Library",
    ),
    WebAuthnExample(
        language="Ruby",
        url="https://github.com/ruby-passkeys/warden-webauthn",
        title="ruby-passkeys/warden-webauthn",
        author="Ruby passkeys",
        type="Library",
    ),
    WebAuthnExample(
        language="Java",
        url="https://github.com/webauthn4j/webauthn4j",
        title="webauthn4j/webauthn4j",
        author="Yoshikazu Nojima",
        type="Library",
    ),
    WebAuthnExample(
        language="Java",
        url="https://github.com/Yubico/java-webauthn-server",
        title="java-webauthn-server",
        author="Yubico",
        type="Library",
    ),
    WebAuthnExample(
        language="Java",
        url="https://github.com/vert-x3/vertx-auth",
        title="vertx-auth/webauthn",
        author="Eclipse Vert.x",
        type="Library",
    ),
    WebAuthnExample(
        language=".NET",
        url="https://github.com/passwordless-lib/fido2-net-lib",
        title="abergs/fido2-net-lib",
        author="Anders Åberg",
        type="Library",
    ),
    WebAuthnExample(
        language="Go",
        url="https://github.com/go-webauthn/webauthn",
        title="go-webauthn/webauthn",
        author="go-webauthn",
        type="Library",
    ),
]

demos = [
    WebAuthnExample(
        language="Python",
        url="https://github.com/duo-labs/webauthn.io",
        title="duo-labs/webauthn.io",
        author="Duo Labs",
        type="Demo",
    ),
    WebAuthnExample(
        language="TypeScript",
        url="https://github.com/google/webauthndemo",
        title="google/webauthndemo",
        author="Google",
        type="Demo",
    ),
    WebAuthnExample(
        language="Javascript",
        url="https://github.com/fido-alliance/webauthn-demo",
        title="webauthn-demo",
        author="FIDO Alliance",
        type="Demo",
    ),
    WebAuthnExample(
        language="Java",
        url="https://github.com/vertx-howtos/fido2-webauthn-howto",
        title="vertx/webauthn-howto",
        author="Eclipse Vert.x",
        type="Demo",
    ),
    WebAuthnExample(
        language=".NET",
        url="https://github.com/passwordless-lib/fido2-net-lib/tree/master/Demo",
        title="passwordless-lib/fido2-net-lib/Demo",
        author="Anders Åberg",
        type="Demo",
    ),
]
