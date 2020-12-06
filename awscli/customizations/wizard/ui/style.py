# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from prompt_toolkit.styles import Style


def get_default_style():
    return Style(
        [
            # Wizard-specific classes
            ('wizard', ''),
            ('wizard.title', 'underline bold'),
            ('wizard.prompt.description', 'bold'),
            ('wizard.prompt.description.current', 'white'),
            ('wizard.prompt.answer', 'bg:#aaaaaa black'),
            ('wizard.prompt.answer.current', 'white'),
            ('wizard.section.tab', 'bold bg:#aaaaaa black'),
            ('wizard.section.tab.current', 'white'),
            ('wizard.section.tab.unvisited', '#777777'),
            ('wizard.section.tab.visited', ''),
            ('wizard.dialog', ''),
            ('wizard.dialog frame.label', 'white bold'),
            ('wizard.dialog.body', 'bg:#aaaaaa black'),
            ('wizard.error', 'bg:#550000 #ffffff'),

            # Prompt-toolkit built-in classes
            ('button.focused', 'bg:#777777 white'),
            ('completion-menu.completion', 'underline'),
            ('shadow', 'bg:#222222'),
        ]
    )
