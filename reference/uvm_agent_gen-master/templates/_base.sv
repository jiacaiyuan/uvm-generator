{% block copyright %}
//-----------------------------------------------------------------------------
{% for line in agent.copyright %}// {{ line }}
{% endfor %}//-----------------------------------------------------------------------------
{% endblock %}

{% block comment_header %}
/**
 * UVM Agent - {{ agent.name }}
 *
 *
 *
 * @file {{ agent.name }}{{ agent.file }}.sv
 * @author {{ agent.author }}
 * @par Contact:
 * {{ agent.email }}
 * @par Company:
 * <a href="{{ agent.href }}">{{ agent.company }}</a>
 *
 */
{% endblock %}

`ifndef {{ agent.name|upper }}{{ agent.file|upper }}__SV
`define {{ agent.name|upper }}{{ agent.file|upper }}__SV

{% block body %}
{% endblock %}

`endif // {{ agent.name|upper }}{{ agent.file|upper }}__SV
